import torch
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, random_split
from torch import nn, optim
import os

# 檢查GPU是否可用
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 定義 CNN 模型
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)  # 第一個卷積層
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)  # 第二個卷積層
        self.pool = nn.MaxPool2d(2, 2)  # 最大池化層
        self.fc1 = nn.Linear(32 * 16 * 16, 128)  # 全連接層
        self.fc2 = nn.Linear(128, 11)  # 輸出層，11個類別

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))  # 卷積、激活和池化
        x = self.pool(torch.relu(self.conv2(x)))
        x = x.view(-1, 32 * 16 * 16)  # 重塑張量
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)  # 輸出層
        return x
    

if __name__ == '__main__':
    
    # 資料增強和標準化
    transform = transforms.Compose([
        transforms.Resize((64, 64)),  # 調整圖片大小
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])

    # 讀取訓練資料集
    train_dataset = torchvision.datasets.ImageFolder(root='train_data', transform=transform)

    # 設定訓練和測試資料的比例
    train_ratio = 0.8
    test_ratio = 0.2

    # 分割訓練和測試資料集
    train_size = int(train_ratio * len(train_dataset))
    test_size = len(train_dataset) - train_size
    train_dataset, test_dataset = random_split(train_dataset, [train_size, test_size])

    # 建立 DataLoader
    train_loader = DataLoader(train_dataset, batch_size=18, shuffle=True, drop_last=True)
    test_loader = DataLoader(test_dataset, batch_size=18, shuffle=False, drop_last=True)
    
    
    # 初始化模型、損失函數和優化器
    model = SimpleCNN().to(device)  # 將模型移動到GPU
    criterion = nn.CrossEntropyLoss()  # 使用交叉熵損失
    optimizer = optim.Adam(model.parameters(), lr=0.001)  # 使用 Adam 優化器

    # 訓練模型
    num_epochs = 5  # 訓練週期
    for epoch in range(num_epochs):
        running_loss = 0.0
        for images, labels in train_loader:
            images = images.to(device)  # 將資料移動到GPU
            labels = labels.to(device)

            optimizer.zero_grad()  # 清空梯度
            outputs = model(images)  # 前向傳播
            loss = criterion(outputs, labels)  # 計算損失
            loss.backward()  # 反向傳播
            optimizer.step()  # 更新權重
            running_loss += loss.item()  # 累計損失

        print(f"Epoch {epoch + 1}, Loss: {running_loss / len(train_loader)}")  # 打印損失

    # 評估模型
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images = images.to(device)  # 將測試資料移動到GPU
            labels = labels.to(device)

            outputs = model(images)  # 前向傳播
            _, predicted = torch.max(outputs, 1)  # 取得最大值的索引
            total += labels.size(0)  # 總樣本數
            correct += (predicted == labels).sum().item()  # 正確預測的數量

    accuracy = correct / total  # 計算準確度
    print(f"Test Accuracy: {accuracy * 100:.2f}%")  # 打印準確度

    # 儲存模型
    torch.save(model.state_dict(), "model.pth")
else:
    # 載入已保存的狀態字典
    model = SimpleCNN()
    model.load_state_dict(torch.load('model.pth'))  # 'simple_cnn.pth' 是先前保存的檔案名

    model.to(device)  # 將模型移動到GPU

    model.eval()  # 設定模型為評估模式