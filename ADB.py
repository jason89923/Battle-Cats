import subprocess
import time
import win32gui
import argparse


argparser = argparse.ArgumentParser()
argparser.add_argument('-p', '--port', type=str, default='62025')
argparser.add_argument('-w', '--window', type=str, default='gugu')
argparser.add_argument('-t', '--threshold', type=int, default=5)

ADB_TOOL_PATH = "C:\\Program Files (x86)\\Nox\\bin\\adb"
IP = '127.0.0.1'
PORT = argparser.parse_args().port
WINDOW_NAME = argparser.parse_args().window
member_level_threshold = argparser.parse_args().threshold  # 0(白) ~ 4(傳說)，小於給定等級就會馬上被踢，5表示啟用隨到隨踢功能


def delay(milliseconds):
    time.sleep(milliseconds/1000)


def send_command(command=[], preDelay=0):
    try:
        delay(preDelay)
        # 構建設置日期和時間的命令
        adb_date_cmd = [ADB_TOOL_PATH, "-s", f"{IP}:{PORT}", *command]
        # 執行命令
        subprocess.run(adb_date_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        pass


class App_base:
    def __init__(self):
        self._click_map = {}

    def click(self, key: str):
        return ['shell', 'input', 'swipe', *[str(i) for i in self._click_map[key]], *[str(i) for i in self._click_map[key]], '40']


class System(App_base):
    reboot = ["reboot"]


class Cat(App_base):
    open = ["shell", "am", "start", "-n",
            "jp.co.ponos.battlecatstw/jp.co.ponos.battlecats.MyActivity"]
    kill = ["shell", "am", "force-stop", "jp.co.ponos.battlecatstw"]

    def __init__(self):
        super().__init__()
        self._click_map['開始遊戲'] = (958, 664)
        self._click_map['章節'] = (951, 662)
        self._click_map['OK'] = (1400, 660)
        self._click_map['進入加碼多多'] = (363, 804)
        self._click_map['加碼多多'] = (950, 680)
        self._click_map['深度探險'] = (1177, 693)
        self._click_map['深度探險_是'] = (740, 750)
        self._click_map['空白'] = (979, 54)
        self._click_map['領取獎勵'] = (1571, 138)
        self._click_map['取消'] = (1456, 195)
        self._click_map['整隊'] = (1673, 163)
        self._click_map['隊員_1'] = (1558, 697)
        self._click_map['隊員_2'] = (235, 697)
        self._click_map['隊員_3'] = (338, 697)
        self._click_map['隊員_4'] = (441, 697)
        self._click_map['隊員_5'] = (544, 697)
        self._click_map['隊員_6'] = (647, 697)
        self._click_map['隊員_7'] = (750, 697)
        self._click_map['隊員_8'] = (1146, 697)
        self._click_map['隊員_9'] = (1249, 697)
        self._click_map['隊員_10'] = (1352, 697)
        self._click_map['隊員_11'] = (1455, 697)
        self._click_map['離隊_取消'] = (1661, 390)
        self._click_map['離隊_是'] = (721, 768)
        self._click_map['離隊'] = (371, 733)
        self._click_map['新隊員'] = (170, 715)
        self._click_map['skip'] = (1774, 1014)


class VPN(App_base):
    open = ["shell", "am", "start", "-n", "eu.faircode.netguard/.ActivityMain"]
    kill = ["shell", "su", "am", "kill", "eu.faircode.netguard"]

    def __init__(self):
        super().__init__()
        self._click_map['switch'] = (170, 95)


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

    def getColor(self, x, y):
        hwndDC = win32gui.GetWindowDC(self._hwnd)
        ret = win32gui.GetPixel(hwndDC, x, y)
        win32gui.ReleaseDC(self._hwnd, hwndDC)
        return "{:06x}".format(ret & 0xffffff).upper()


class Triple_Pixel_Info:
    def __init__(self, coord1, color1, coord2, color2, coord3, color3) -> None:
        self.coord1 = coord1
        self.color1 = color1
        self.coord2 = coord2
        self.color2 = color2
        self.coord3 = coord3
        self.color3 = color3


COLOR_MAP = {
    '加碼多多圖示': Triple_Pixel_Info((347, 710), "000000", (364, 772), "43C1DA", (347, 753), "226495"),
    '加碼多多鈴鐺': Triple_Pixel_Info((1598, 87), "FFFFFF", (1776, 69), "00B7F3", (1783, 89), "00A4DF"),
    '加碼多多換裝': Triple_Pixel_Info((1714,166), "FFFFFF", (1769,177), "FFFFFF", (1740,176), "42CEFF"),
    '喵力達': Triple_Pixel_Info((823, 699), "DB910A", (940, 688), "FFFFFF", (1071, 698), "45D5E0"),
    '6小時深度探險按鈕': Triple_Pixel_Info((1022, 683), "00B9F6", (1083, 660), "000000", (1192, 687), "FFFFFF"),
    '深度探險(是)': Triple_Pixel_Info((623, 780), "009BD6", (639, 720), "00C1FF", (748, 758), "05020B"),
    '滿員彈窗': Triple_Pixel_Info((537, 598), "1B2224", (783, 514), "FEFEFE", (1346, 490), "233338"),
    '確認出發(是)': Triple_Pixel_Info((629, 718), "00C1FF", (641, 785), "0096D0", (789, 736), "00C1FF"),
    '離隊彈窗': Triple_Pixel_Info((1544, 686), "0000FF", (1545, 394), "00B6F3", (380, 598), "1B2224"),
    '離隊確認彈窗': Triple_Pixel_Info((633, 716), "00C1FF", (825, 743), "00BEFB", (720, 760), "FFFFFF"),
    '白色隊員': Triple_Pixel_Info((942, 194), "FFFFFF", (920, 198), "FFFFFF", (969, 217), "FFFFFF"),
    '銅色隊員': Triple_Pixel_Info((938, 193), "2467CC", (970, 199), "4566BA", (911, 213), "4567BC"),
    '銀色隊員': Triple_Pixel_Info((941, 192), "BAB2A0", (918, 216), "DACEB2", (968, 199), "B9B19F"),
    '鑽石隊員': Triple_Pixel_Info((912, 216), "86F6A7", (964, 195), "F2C8A9", (950, 213), "E99DE9"),
    '新隊員提示': Triple_Pixel_Info((969, 233), "FFFFFF", (934, 228), "FFFFFF", (909, 231), "FFFFFF"),
    'skip畫面': Triple_Pixel_Info((1607, 942), "00C1FF", (1645, 961), "FFFFFF", (1783, 961), "00BFFD"),
    'VPN': Triple_Pixel_Info((225, 121), '2155FA', (336, 117), '889600', (488, 116), '889600'),
    'VPN背景': Triple_Pixel_Info((610, 106),  '889600', (857, 113),  '889600', (1158, 115),  '889600')
}


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


check_Pixel_Info = Check_Pixel_Info()


def corruptRecovery():
    deadline = 0

    deadline = deadline + 1

    if deadline == 3:
        send_command(Commands.System.reboot)
        delay(30000)  # wait 30 seconds to restart
        deadline = 0
        delay(100)

    send_command(Commands.App.CAT.kill)
    send_command(Commands.App.VPN.kill)

    send_command(Commands.Time.auto_get_date_off)
    send_command(Commands.Time.auto_get_date_on)

    send_command(Commands.App.VPN.open)
    send_command(Commands.App.CAT.open)

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
                while check_Pixel_Info.check('深度探險(是)'):  # 出現是否出發前一直點深度探險
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

            #for i in range(3):
             #   send_command(Commands.App.CAT.click('空白'))  # 點空白

            send_command(Commands.App.VPN.open)
            if not check_Pixel_Info.check('VPN', 100):
                send_command(Commands.App.VPN.click('switch'))
            send_command(Commands.App.VPN.click('switch'))
            send_command(Commands.Time.set_date)
            send_command(Commands.App.CAT.open)
            send_command(Commands.App.VPN.open, 50)
            send_command(Commands.Time.auto_get_date_off)
            send_command(Commands.Time.auto_get_date_on)
            send_command(Commands.App.VPN.click('switch'))
            send_command(Commands.App.CAT.open)
            
            if check_Pixel_Info.check_response('加碼多多鈴鐺'):
                corruptRecovery()
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

                    if i >= 100:
                        raise Exception('keep going')  # 繼續原本的流程
                    i = i + 1

                i = 0
                while check_Pixel_Info.check('離隊確認彈窗', 50):  # 判斷是否出現離隊確認彈窗
                    send_command(Commands.App.CAT.click('離隊'))
                    i = i + 1
                    if i == 30:
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
            print(f'第 {counter} 次執行耗時： {time.time() - start_time:.3f}s')
            start_time = time.time()
            counter += 1
        error = False
            
