import pyautogui
import time
from PIL import ImageOps
import torch
from torchvision import transforms
import model

# 定義獲取截圖的函數
def get_screenshot(x1, y1, x2, y2):
    # 計算截圖的區域
    region = (x1, y1, x2 - x1, y2 - y1)
    # 獲取截圖
    screenshot = pyautogui.screenshot(region=region)
    return screenshot

# 數字的固定寬度和高度
digit_width = 45  # 每個數字的寬度
digit_height = 64  # 每個數字的高度

def split(screenshot):   
    
    # 第五位數字的右上角座標和左下角座標
    start_x = 307
    start_y = 5
    end_x = 262
    end_y = 69

    # 每個數字之間的差距
    step = 45  # 每個數字的寬度
    
    all_digits = []
    # 切割並儲存每個數字
    for i in range(5):
        # 計算每個數字的左上角和右下角座標
        left = start_x - i * step
        upper = start_y
        right = left - digit_width
        lower = end_y

        # 切割數字
        digit = screenshot.crop((right, upper, left, lower))
        
        # 裁剪圖像以去除左右多餘部分
        digit = digit.crop((2, 0, digit_width - 4, digit_height))
        
        # 二值化
        digit = digit.convert("L")  # 轉換為灰階
        digit = ImageOps.invert(digit)  # 反轉顏色
        digit = ImageOps.autocontrast(digit)  # 自動增強對比度
        digit = digit.convert('RGB')
        all_digits.append(digit)
    return all_digits


# 預測函數
def predict_digits(digits):
    # 定義轉換
    transform = transforms.Compose([
        transforms.Resize((64, 64)),  # 調整圖片大小
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])

    # 初始化預測結果
    predictions = []

    # 對於每個數字，執行預測
    for digit in digits:
        # 轉換數字為張量
        tensor = transform(digit)
        tensor = tensor.to(model.device)  # 移動到GPU

        # 執行預測
        with torch.no_grad():
            output = model.model(tensor)  # 模型前向傳播
            _, predicted = torch.max(output, 1)  # 獲取最大值的索引
            mosst_possible = predicted.item()
            if mosst_possible != 10:
                predictions.insert(0, mosst_possible)  # 將預測結果插入到列表的開頭
    return int(''.join(map(str, predictions))) if len(predictions) > 0 else 0

def detect_can():
    screenshot = get_screenshot(1509, 951, 1825, 1028)
    all_digits = split(screenshot)
    # 預測數字
    num_of_can = predict_digits(all_digits)  # 預測每個數字
    return num_of_can


if __name__ == '__main__':
    while True:
        detect_can()

        time.sleep(8)  # 根據需求調整間隔時間