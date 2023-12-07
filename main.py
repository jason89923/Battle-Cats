import subprocess
import time
import win32gui
import win32con
import argparse
import json
import threading
import discord
import asyncio
from datetime import datetime


TOKEN = ""

CURRENT_CHANNEL = '二號機'
CHANNEL = {'一號機': 1181625760222543883, '二號機': 1182266933018628136, '三號機': 1182266968749899807}



intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def monitor_event_and_send_message(channel):
    await channel.send(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {CURRENT_CHANNEL}已就緒")
    # 監控邏輯
    while not client.is_closed():
        if condition_is_met():
            await channel.send(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {CURRENT_CHANNEL}超過 4 分鐘沒有回應，請盡快處理')
        await asyncio.sleep(240)

def condition_is_met():
    if time.time() - last_success_time > 240:
        return True
    return False

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    channel = client.get_channel(CHANNEL[CURRENT_CHANNEL])  # 用實際的頻道 ID 替換
    client.loop.create_task(monitor_event_and_send_message(channel))


def start():
    client.run(TOKEN)  # 用您的 Bot 令牌替換


last_success_time = time.time()

bot_thread = threading.Thread(target=start)
bot_thread.daemon = True  # 将线程设置为守护线程
bot_thread.start()


argparser = argparse.ArgumentParser()
argparser.add_argument('-p', '--port', type=str, default='5556')
argparser.add_argument('-w', '--window', type=str, default='jason')
argparser.add_argument('-t', '--threshold', type=int, default=5)
argparser.add_argument('-c', '--config', type=str, default='')

ADB_TOOL_PATH = "adb"
TAG = f'emulator-{argparser.parse_args().port}'
WINDOW_NAME = argparser.parse_args().window
# 0(白) ~ 4(傳說)，小於給定等級就會馬上被踢，5表示啟用隨到隨踢功能
member_level_threshold = argparser.parse_args().threshold
CONFIG = argparser.parse_args().config


def delay(milliseconds):
    time.sleep(milliseconds/1000)


def send_command(command=[], preDelay=0):
    try:
        delay(preDelay)
        # 構建設置日期和時間的命令
        adb_date_cmd = [ADB_TOOL_PATH, "-s", f"{TAG}", *command]
        # 執行命令
        subprocess.run(adb_date_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=1)
    except Exception as e:
        corruptRecovery(need_reboot=True)
        
def adb_ready():
    subprocess.run([ADB_TOOL_PATH, 'kill-server'])
    subprocess.run([ADB_TOOL_PATH, 'start-server'])
    for i in range(30):
        result = subprocess.run([ADB_TOOL_PATH, 'devices'], stdout=subprocess.PIPE, text=True)
        lines = result.stdout.strip().split('\n')[1:]
        state = None
        for line in lines:
            if TAG in line:
               name, state = line.split()
               break
        print(f'第{i}秒狀態: {state}')
        if state == 'device':
            return
        delay(1000)
    

class App_base:
    def __init__(self):
        self._click_map = {}

    def click(self, key: str):
        return ['shell', 'input', 'swipe', *[str(i) for i in self._click_map[key]], *[str(i) for i in self._click_map[key]], '40']


class System(App_base):
    reboot = ['shell', 'reboot']


class Cat(App_base):
    open = ["shell", "am", "start", "-n",
            "jp.co.ponos.battlecatstw/jp.co.ponos.battlecats.MyActivity"]
    kill = ["shell", "am", "force-stop", "jp.co.ponos.battlecatstw"]

    def __init__(self):
        super().__init__()
        self._click_map['開始遊戲'] = (956, 533)# ok
        self._click_map['章節'] = (956, 533)# ok
        self._click_map['OK'] = (1185, 538)# ok
        self._click_map['進入加碼多多'] = (301, 673)
        self._click_map['加碼多多'] = (800, 572)  # ok
        self._click_map['深度探險'] = (980, 591)  # ok
        self._click_map['深度探險_是'] = (603, 640)  # ok
        self._click_map['空白'] = (818, 37)  # ok
        self._click_map['領取獎勵'] = (1332, 119) # ok
        self._click_map['取消'] = (1199, 139) # ok
        self._click_map['整隊'] = (1364, 137) # ok
        # 還沒弄
        self._click_map['隊員_1'] = (1291, 570)
        self._click_map['隊員_2'] = (278, 570)
        self._click_map['隊員_3'] = (359, 570)
        self._click_map['隊員_4'] = (450, 570)
        self._click_map['隊員_5'] = (524, 570)
        self._click_map['隊員_6'] = (621, 570)
        self._click_map['隊員_7'] = (750, 570)
        self._click_map['隊員_8'] = (1146, 570)
        self._click_map['隊員_9'] = (1249, 570)
        self._click_map['隊員_10'] = (1352, 570)
        self._click_map['隊員_11'] = (1455, 570)
        self._click_map['離隊_取消'] = (1378, 313) # ok
        self._click_map['離隊'] = (386, 626) # ok
        self._click_map['離隊_是'] = (693, 659)# ok
        # 還沒弄
        self._click_map['新隊員'] = (83, 591) # ok
        self._click_map['skip'] = (1417, 821) # ok


class VPN(App_base):
    open = ["shell", "am", "start", "-n", "eu.faircode.netguard/.ActivityMain"]
    kill = ["shell", "su", "am", "kill", "eu.faircode.netguard"]

    def __init__(self):
        super().__init__()
        self._click_map['switch'] = (148, 78)
        self._click_map['返回'] = (53, 81)


class Commands:
    class Time:
        set_date = ["shell", "su", "0", "date", "111208302021.25"]
        auto_get_date_off = ['shell', 'settings',
                             'put', 'global', 'auto_time', '0']
        auto_get_date_on = ['shell', 'settings',
                            'put', 'global', 'auto_time', '1']

    class App:
        CAT = Cat()
        VPN = VPN()
        System = System()


class BKWindow:

    def __init__(self, WindowsName):
        self._originalWindonsName = WindowsName
        self._WindonsName = WindowsName
        self._hwnd = win32gui.FindWindow(None, WindowsName)
        if self._hwnd == 0:
            raise ValueError("WindowsNanme Not Found")
        self.maximize()

    def getColor(self, x, y):
        hwndDC = win32gui.GetWindowDC(self._hwnd)
        ret = win32gui.GetPixel(hwndDC, x, y)
        win32gui.ReleaseDC(self._hwnd, hwndDC)
        return "{:06x}".format(ret & 0xffffff).upper()
    
    def maximize(self):
        win32gui.ShowWindow(self._hwnd, win32con.SW_MAXIMIZE)


class Triple_Pixel_Info:
    def __init__(self, coord1, color1, coord2, color2, coord3, color3) -> None:
        self.coord1 = coord1
        self.color1 = color1
        self.coord2 = coord2
        self.color2 = color2
        self.coord3 = coord3
        self.color3 = color3
    
    @staticmethod
    def encode(obj):
        if isinstance(obj, Triple_Pixel_Info):
            return {
                "coord1": obj.coord1,
                "color1": obj.color1,
                "coord2": obj.coord2,
                "color2": obj.color2,
                "coord3": obj.coord3,
                "color3": obj.color3
            }
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")
        
    @staticmethod
    def to_obj(d):
        return Triple_Pixel_Info(d['coord1'], d['color1'], d['coord2'], d['color2'], d['coord3'], d['color3'])

if CONFIG == '':
    COLOR_MAP = {
        '加碼多多黑畫面': Triple_Pixel_Info((395,173),  '000000', (777,181),  '000000', (1364,181),  '000000'),
        '加碼多多圖示': Triple_Pixel_Info((415, 764), "FFFFFF", (404, 764), "FFFFFF", (332, 732), "363636"),
        '加碼多多鈴鐺': Triple_Pixel_Info((1580, 91), "FFFFFF", (1586, 84), "FFFFFF", (1591, 87), "FFFFFF"),
        '加碼多多換裝': Triple_Pixel_Info((1715, 167), "FFFFFF", (1764, 175), "FFFFFF", (1727, 201), "42CEFF"),
        '喵力達': Triple_Pixel_Info((835,678), '3963C9', (953,683), '2E509B', (1074,679), '436CD2'),
        '6小時深度探險按鈕': Triple_Pixel_Info((1008, 650),  '00C2FF', (1143, 696),  'EDEDED', (1303, 700), '00A2DE'),
        '確認出發(是)': Triple_Pixel_Info((637, 719), '00C1FF', (792, 734),  '00BFFF', (801, 779),  '0097D1'),
        '滿員彈窗': Triple_Pixel_Info((753,496),  '8F9699', (947,520),  'FBFBFB', (1007,554),  'F7F8F8'),#ok
        '離隊彈窗': Triple_Pixel_Info((493,699), '00C2FF', (339,692), '00C2FF', (344,726), '00A5E0'),#ok
        '離隊確認彈窗': Triple_Pixel_Info((643,728), '00C1FF', (645,770), '009FDA', (781,772), '009ED9'),#ok
        '白色隊員': Triple_Pixel_Info((941,193), "FFFFFF", (931,216), "FFFFFF", (968,200), "FFFFFF"), #ok
        '銅色隊員': Triple_Pixel_Info((1074,679), '436CD2', (933,213), '2267CD', (966,197), '3D66BF'), #ok
        '銀色隊員': Triple_Pixel_Info((939,193),  'B9B19F', (970,199),  'AFA18D', (933,215),  'B9B19F'), #ok
        '鑽石隊員': Triple_Pixel_Info((912,211), 'C3EDCC', (956,195), 'EFE9F1', (966,212), '9FB4CB'), #ok
        '新隊員提示': Triple_Pixel_Info((963,233), "FFFFFF", (907,235), "FFFFFF", (957,245), "FFFFFF"),#ok
        'skip畫面': Triple_Pixel_Info((1589,935),  '00C1FF', (1591,999),  '0095CF', (1763,977),  '00ACE8'),  #ok
        'VPN': Triple_Pixel_Info((232, 133), '2155FA', (232, 124), '2155FA', (240, 123), '2155FA'),  #ok
        'VPN背景': Triple_Pixel_Info((555, 111),  '889600', (685, 115),  '889600', (933, 124),  '889600'),  #ok
        'VPN正常': Triple_Pixel_Info((149,116), 'FFFFFF', (148,131), '889600', (132,136), 'FFFFFF')
    }
else:
    with open(CONFIG, 'r', encoding='utf8') as f:
        d = json.load(f)
    COLOR_MAP = {key : Triple_Pixel_Info.to_obj(d[key]) for key in d}


class Check_Pixel_Info:
    window = BKWindow(WINDOW_NAME)

    def check(self, point_tag: str, preDelay=0):
        delay(preDelay)
        triple_pixel_info = COLOR_MAP[point_tag]
        if self.window.getColor(*triple_pixel_info.coord1) == triple_pixel_info.color1 and self.window.getColor(*triple_pixel_info.coord2) == triple_pixel_info.color2 and self.window.getColor(*triple_pixel_info.coord3) == triple_pixel_info.color3:
            return False
        return True

    def check_response(self, point_tag: str, preDelay=0):
        delay(preDelay)
        triple_pixel_info = COLOR_MAP[point_tag]
        for i in range(300):
            if self.window.getColor(*triple_pixel_info.coord1) == triple_pixel_info.color1 and self.window.getColor(*triple_pixel_info.coord2) == triple_pixel_info.color2 and self.window.getColor(*triple_pixel_info.coord3) == triple_pixel_info.color3:
                return False
            delay(10)
        return True
    
    def update_window(self):
        self.window = BKWindow(WINDOW_NAME)


check_Pixel_Info = Check_Pixel_Info()

def corruptRecovery(need_reboot=False):

    if need_reboot:
        send_command(Commands.App.System.reboot)
        delay(10000)
        adb_ready()
        check_Pixel_Info.update_window()
        
    for i in range(3):

        send_command(Commands.App.CAT.kill)
        send_command(Commands.App.VPN.kill)

        send_command(Commands.Time.auto_get_date_off)
        send_command(Commands.Time.auto_get_date_on)

        send_command(Commands.App.VPN.open)
        send_command(Commands.App.CAT.open)
        if not check_Pixel_Info.check_response('加碼多多黑畫面'):
            break

    for i in range(5):
        send_command(Commands.App.CAT.click('skip'), 300)

    i = 0
    while check_Pixel_Info.check('skip畫面', 10):
        i = i + 1
        if i == 700:
            raise Exception('corrupt recovery')

    send_command(Commands.App.CAT.click('skip'))  # 點擊skip

    delay(1000)

    i = 0
    while check_Pixel_Info.check('加碼多多圖示', 50):
        send_command(Commands.App.CAT.click('開始遊戲'))
        send_command(Commands.App.CAT.click('章節'))
        send_command(Commands.App.CAT.click('OK'))
        i = i + 1
        if i >= 150:
            raise Exception('corrupt recovery')

    send_command(Commands.App.CAT.click('進入加碼多多'), 500)
    check_Pixel_Info.check_response('加碼多多鈴鐺')
    delay(400)
    raise Exception('corrupt recovery')


def keepLargest():
    global member_level_threshold
    smallest = [10, 10]

    send_command(Commands.App.CAT.click('取消'))
    send_command(Commands.App.CAT.click('取消'), 600)
    send_command(Commands.App.CAT.click('整隊'), 600)
    delay(3500)

    kick_off = False
    for i in range(11):
        send_command(Commands.App.CAT.click(f'隊員_{i + 1}'))  # 點要檢查的隊員
        j = 0
        while check_Pixel_Info.check('離隊彈窗', 400):  # 判斷是否出現隊員資訊彈窗
            send_command(Commands.App.CAT.click(f'隊員_{i + 1}'))  # 點要檢查的隊員
            j = j + 1
            if j == 5:
                return

        delay(100)
        if not check_Pixel_Info.check('白色隊員'):
            currentLevel = 0
        elif not check_Pixel_Info.check('銅色隊員'):
            currentLevel = 1
        elif not check_Pixel_Info.check('銀色隊員'):
            currentLevel = 2
        elif not check_Pixel_Info.check('鑽石隊員'):
            currentLevel = 4
        else:
            currentLevel = 3

        if currentLevel <= smallest[0]:
            smallest[0] = currentLevel
            smallest[1] = i

        if currentLevel < member_level_threshold:
            kick_off = True
            break

        send_command(Commands.App.CAT.click('離隊_取消'))
        delay(400)

    if not kick_off:
        send_command(Commands.App.CAT.click(f'隊員_{smallest[1] + 1}'))
        delay(400)
        member_level_threshold = smallest[0] + 1

    i = 0
    while check_Pixel_Info.check('離隊確認彈窗', 10):  # 判斷是否出現離隊確認彈窗
        send_command(Commands.App.CAT.click('離隊'))
        i = i + 1
        if i == 60:
            return

    i = 0
    while check_Pixel_Info.check('加碼多多鈴鐺', 400):  # 判斷是否出現離隊確認彈窗
        send_command(Commands.App.CAT.click('離隊_是'))
        i = i + 1
        if i == 20:
            return
    raise Exception('kick off')


if __name__ == '__main__':
    adb_ready()
    error = False
    counter = 0
    start_time = time.time()
    while True:
        try:
            skip = False
            if check_Pixel_Info.check_response('加碼多多鈴鐺'):  # 判斷是否在加碼多多的畫面(換裝)
                corruptRecovery()

            if not check_Pixel_Info.check('喵力達'):  # 已經開始(喵力達)
                skip = True

            if not skip:
                i = 0
                # 如果沒出現6小時深度探險按鈕，就一直點加碼多多
                while check_Pixel_Info.check('6小時深度探險按鈕'):
                    send_command(Commands.App.CAT.click('加碼多多'))
                    delay(100)
                    i += 1
                    if i > 30:
                        corruptRecovery()

                i = 0
                while check_Pixel_Info.check('確認出發(是)'):  # 出現是否出發前一直點深度探險
                    if i % 3 == 0:
                        send_command(Commands.App.CAT.click('深度探險'))
                    i += 1

                    if i > 15:
                        corruptRecovery()

                    if not check_Pixel_Info.check('滿員彈窗', 200):  # 滿員(暫時判不了)
                        keepLargest()

                i = 0
                # 如果確認出發前的彈窗還沒消失，就一直點確認出發(是)
                while not check_Pixel_Info.check('確認出發(是)'):
                    send_command(Commands.App.CAT.click('深度探險_是'))
                    delay(100)
                    i += 1

                    if i > 30:
                        corruptRecovery()

            for i in range(7):
                send_command(Commands.App.CAT.click('空白'))  # 點空白

            send_command(Commands.App.VPN.open)
            send_command(Commands.App.VPN.click('返回'))
            if not check_Pixel_Info.check('VPN'):
                send_command(Commands.App.VPN.click('switch'))
            send_command(Commands.App.VPN.click('switch'))
            send_command(Commands.Time.set_date)
            send_command(Commands.App.CAT.open)
            send_command(Commands.App.VPN.open, 1000)
            send_command(Commands.Time.auto_get_date_off)
            send_command(Commands.Time.auto_get_date_on)
            send_command(Commands.App.VPN.click('switch'))
            send_command(Commands.App.CAT.open)
                
            #if check_Pixel_Info.check_response('加碼多多鈴鐺'):
                #corruptRecovery()
            delay(200)
            is_new_member = False
            i = 0
            while check_Pixel_Info.check('加碼多多換裝', 20):
                send_command(Commands.App.CAT.click('領取獎勵'))
                if not check_Pixel_Info.check('新隊員提示'):  # 判斷是否出現新隊員提示
                    is_new_member = True
                    break
                if not check_Pixel_Info.check('喵力達'):
                    raise Exception('重來')  # 繼續原本的流程

                if i >= 100:
                    corruptRecovery()
                i = i + 1

            if member_level_threshold == 5 and is_new_member:  # 如果已經全傳說隊員，並且發現新隊員，就直接踢掉
                i = 0
                while check_Pixel_Info.check('離隊彈窗'):  # 離隊按鈕
                    send_command(Commands.App.CAT.click('新隊員'))  # 嘗試抓到新進隊員

                    if i >= 70:
                        raise Exception('keep going')  # 繼續原本的流程
                    i = i + 1

                i = 0
                while check_Pixel_Info.check('離隊確認彈窗'):  # 判斷是否出現離隊確認彈窗
                    send_command(Commands.App.CAT.click('離隊'))
                    i = i + 1
                    if i == 60:
                        raise Exception('keep going')  # 繼續原本的流程

                i = 0
                while check_Pixel_Info.check('加碼多多鈴鐺', 400):  # 判斷是否出現離隊確認彈窗
                    send_command(Commands.App.CAT.click('離隊_是'))
                    i = i + 1
                    if i == 20:
                        raise Exception('keep going')  # 繼續原本的流程
            elif is_new_member:
                for i in range(10):
                    send_command(Commands.App.CAT.click('空白'))  # 點空白
        except Exception as e:
            if e.args[0] != 'keep going':
                error = True
        if not error:
            last_success_time = time.time()
            print(f'第 {counter} 次執行耗時： {time.time() - start_time:.3f}s')
            start_time = time.time()
            counter += 1
        error = False
