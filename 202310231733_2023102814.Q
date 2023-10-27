[General]
SyntaxVersion=2
BeginHotkey=121
BeginHotkeyMod=0
PauseHotkey=0
PauseHotkeyMod=0
StopHotkey=123
StopHotkeyMod=0
RunOnce=1
EnableWindow=
MacroID=6011f205-ad53-42ff-b076-3f09c5f9c7f6
Description=罐頭多多
Enable=0
AutoRun=0
[Repeat]
Type=1
Number=1
[SetupUI]
Type=2
QUI=
[Relative]
SetupOCXFile=
[Comment]

[Script]

Function click(key, preDelay, hwndChild)
	Delay preDelay
	Call Plugin.Bkgnd.KeyDown(hwndChild, key)
	Delay 70
	Call Plugin.Bkgnd.KeyUp(hwndChild,key)
	Delay 20
End Function

Function threePointCheck(x1, y1, color1, x2, y2, color2, x3, y3, color3, preDelay, hwnd)
	Delay preDelay

	If color1 = Plugin.Bkgnd.GetPixelColor(hwnd, x1, y1) And color2 = Plugin.Bkgnd.GetPixelColor(hwnd, x2, y2) And color3 = Plugin.Bkgnd.GetPixelColor(hwnd, x3, y3)  Then 
		threePointCheck = False
		
	Else 
		threePointCheck = True
		
	End If
End Function

Function threePointCheck_respond(x1, y1, color1, x2, y2, color2, x3, y3, color3, hwnd)
	// 響應式
	i = 0
	While color1 <> Plugin.Bkgnd.GetPixelColor(hwnd, x1, y1) Or color2 <> Plugin.Bkgnd.GetPixelColor(hwnd, x2, y2) Or color3 <> Plugin.Bkgnd.GetPixelColor(hwnd, x3, y3)
		
		i = i + 1
		
		If i > 30 Then 
			threePointCheck_respond = True
			Goto endRespond
		End If
		
		Delay 100
	Wend

	threePointCheck_respond = False
	Rem endRespond
	
End Function

Function home(hwndChild, preDelay)
	Call click(112, preDelay, hwndChild)
End Function

Function currentMission(hwndChild, preDelay)
	Call click(113, preDelay, hwndChild)
End Function

Function backHome(hwndChild,hwnd)
	Rem home
	Call home(hwndChild, 50)
	If threePointCheck(532,558, "4FF9FF", 533,537, "3123FF", 566,542 , "2073F2", 100, hwnd) Then 
		Goto home
	End If
End Function

Function corruptRecovery(hwndChild, hwnd)
	Rem e1
	Rem e2
	Rem e3
	
	If threePointCheck(537,551, "889600", 631,556, "212121", 551,654, "8F9C0E", 0, hwnd) = False Then // 桌面閃退
			Call click(187, 0, hwndChild)// 重啟桌面
			Delay 2000
			Goto e3
	End If
	
	
	Call currentMission(hwndChild, 500)

	Call click(114, 1500, hwndChild)
	Call click(114, 1500, hwndChild)
	Call click(65, 800, hwndChild)
	Delay 500
	Call backHome(hwndChild, hwnd)
	
	Call click(67, 0, hwndChild)
	
	If threePointCheck(115, 564, "889600", 189, 580, "737373", 304, 556, "212121", 1000, hwnd) = False Then 
		Goto e3
	End If
	
	For 4
		Call click(114, 1000, hwndChild)
	Next
	
	Call click(65, 1000, hwndChild)
	
	If threePointCheck(306,264, "737373", 197,253, "848484", 174,253, "7D7D7D", 600, hwnd) Then // 設定 初始校驗
		Goto e1
	End If
	
	Call click(68, 300, hwndChild) // auto time & date
	Call click(68, 300, hwndChild) // auto time & date
	
	Rem wall1
	Rem wall2
	
	Call backHome(hwndChild, hwnd)
	
	Call click(66, 0, hwndChild)
	
	If threePointCheck(554,132, "F9CA90", 551,424, "FAFAFA", 481,970, "F5A542", 500, hwnd) Then // vpn 初始校驗
		Goto wall1
	End If
	
	Call click(66, 0, hwndChild)
	
	If threePointCheck(848,265, "53C800", 852,332, "53C800", 1021,336, "53C800", 500, hwnd) Then // vpn 結束校驗
		Goto wall2
	End If
	
	Call backHome(hwndChild, hwnd)
	
	Call click(65, 0, hwndChild)
	
	For 5
		Call click(65, 300, hwndChild)
	Next
	
	i = 0
	While threePointCheck(1597,950, "00C1FF", 1676,975, "FFFFFF", 1703,983, "000000", 50, hwnd)  //skip
		If i >= 100 Then 
			Goto e2
		End If
		i = i + 1
	Wend
		
	
	Call click(73, 0, hwndChild)
	
	i = 0
	While threePointCheck(347,710, "000000", 364,772, "43C1DA", 347,753, "226495", 50, hwnd)//加碼多多
	  	Call click(65, 0, hwndChild)
	  	Call click(71, 10, hwndChild)
		If i >= 30 Then 
			Goto e3
		End If
		i = i + 1
	Wend
	Call click(74, 0, hwndChild)
	Delay 1800
End Function

Function findInputHwnd(hwnd)
	nextChild = Plugin.Window.FindEx(hwnd, 0, 0, "Nox")
	child = 0
	While nextChild <> 0
		child = nextChild
		nextChild = Plugin.Window.FindEx(hwnd, child, 0, 0)
	Wend
	
	findInputHwnd = Plugin.Window.FindEx(child, 0, 0, 0)
End Function

Function keepLargest(hwndChild, hwnd, max, min)

	keepLargest = min

    smallest = Array(10, 10)

	Call click(70, 0, hwndChild) // 取消
	Call click(70, 600, hwndChild) // 取消
	Call click(69, 600, hwndChild)// 整隊
	Call click(69, 300, hwndChild)// 整隊
	Call click(69, 300, hwndChild)// 整隊
	Delay 3500
	
	currentLevel = 0

    i = 90
    For 11
    	Call click(i, 0, hwndChild) // 點要檢查的隊員
    	j = 0
    	While threePointCheck(1544,686, "0000FF", 1545,394, "00B6F3", 380,598, "1B2224", 400, hwnd)
    		Call click(i, 0, hwndChild)
    		j = j + 1
    		If j = 5 Then 
    			Goto endFunction
    		End If
    	Wend
        
        Delay 100
        If threePointCheck(936,192, "B8AF9B", 931,213, "B9B19F", 952,195, "ECE2D0", 0, hwnd) = False Then
        	currentLevel = 2 // 銀
        Elseif threePointCheck(944,194, "38CBEA", 915,212, "37CEEE", 942,213, "38CBEA", 0, hwnd) = False Then
        	currentLevel = 3 // 金
        Elseif threePointCheck(940,192, "FFFFFF", 914,214, "FFFFFF", 967,218, "FFFFFF", 0, hwnd) = False Then
        	currentLevel = 0 // 白
        Elseif threePointCheck(911,215, "4364B9", 932,211, "236BD5", 946,194, "8DB0E6", 0, hwnd) = False Then
        	currentLevel = 1 // 銅
        Else 
        	currentLevel = 4 // 傳說
        End If
        
        If currentLevel <= smallest(0) Then 
        	smallest(0) = currentLevel
        	smallest(1) = i
        End If
        
        If currentLevel < min or currentLevel > max Then 
        	Goto e
        End If

        Call click(75, 0, hwndChild)
        Delay 400
        
        i = i - 1
    Next
    
    Call click(smallest(1), 0, hwndChild)
    Delay 400
	keepLargest = smallest(0) + 1
    
    Rem e
    Call click(72, 0, hwndChild) // 離隊
	Call click(67, 400, hwndChild) // 是
	Call click(67, 400, hwndChild)// 是
	Delay 400
	Rem endFunction
End Function

Function main(name, max, min)
	hwnd = Plugin.Window.Find("Qt5QWindowIcon", name)
	hwndChild = findInputHwnd(hwnd)
	vpnCounter = 0
	vpnMAX = 15
	
	While True
		Rem start
		
		If threePointCheck(537,551, "889600", 631,556, "212121", 551,654, "8F9C0E", 0, hwnd) = False Then // 桌面閃退
			Call click(187, 0, hwndChild)// 重啟桌面
			Delay 2000
			Goto start
		End If
		
		vpnCounter = vpnCounter + 1
		
		Call click(68, 0, hwndChild)// white
		
		If threePointCheck(1778,98, "009BD6", 1775,68, "00B8F4", 1596,81, "FFFFFF", 300, hwnd) Then // 判斷是否在加碼多多的畫面
			Call corruptRecovery(hwndChild, hwnd)
			vpnCounter = 0
			Goto start
		End If
		
		If threePointCheck(816,707, "FFFFFF", 930,698, "4545C9", 1072,698, "40C6D7", 0, hwnd) = False Then // 已經開始(喵力達)
			Goto skip
		End If
		
		i = 0
		While threePointCheck(567,327, "90E2FF", 604,264, "2D4C8E", 504,267, "2C4989", 0, hwnd) // 貓咪 start校驗
			Call click(65, 0, hwndChild)// 點加碼多多準備開始
			Delay 100
			i = i + 1
			
			If i > 30 Then 
				Call corruptRecovery(hwndChild, hwnd)
				vpnCounter = 0
				Goto start
			End If
		Wend
		
		i = 0
		While threePointCheck(620, 731, "00C1FF", 616, 784, "0098D2", 806, 772, "00A2DC", 0, hwnd)// 出現是否出發前一直點深度探險
			If i Mod 3 = 0 Then
				Call click(66, 0, hwndChild)// 點深度探險
			End If
			i = i + 1
			
			If i > 15 Then 
				Call corruptRecovery(hwndChild, hwnd)
				vpnCounter = 0
				Goto start
			End If
			
			If threePointCheck(520,584, "1C2426", 925,558, "FFFFFF", 1226,579, "1C2527", 200, hwnd) = False Then // 滿員
				min = keepLargest(hwndChild, hwnd, max, min)
				vpnCounter = vpnCounter - 1
				Goto start
		End If
		Wend
	
		i = 0
		While threePointCheck(620,731, "00C1FF", 616,784, "0098D2", 806,772, "00A2DC", 0, hwnd) = False // 如果確認出發前的彈窗還沒消失，就一直點確認出發
			Call click(67, 0, hwndChild)// 點確認出發
			Delay 100
			i = i + 1
			
			If i > 30 Then 
				Call corruptRecovery(hwndChild, hwnd)
				vpnCounter = 0
				Goto start
			End If
		Wend
		
		i = 0
		While threePointCheck(816,707, "FFFFFF", 930,698, "4545C9", 1072,698, "40C6D7", 0, hwnd) // 判斷是否已經出發去探險
		    Call click(68, 0, hwndChild)// 空白
		    Delay 100
		    i = i + 1
		    If i > 5 Then 
		    	Call corruptRecovery(hwndChild, hwnd)
				vpnCounter = 0
				Goto start
		    End If
		Wend
		
		
		Rem skip
		
		If vpnCounter = 1 Then 
			Rem wall
			Call backHome(hwndChild, hwnd)	
			
			Call click(66, 0, hwndChild) // vpn
			
			If threePointCheck(554,132, "F9CA90", 551,424, "FAFAFA", 481,970, "F5A542", 500, hwnd) Then // vpn 初始校驗
				Goto wall
			End If
			
			Call click(65, 0, hwndChild) // vpn start
			
			If threePointCheck(847,621, "2F2FD3", 851,683, "2F2FD3", 1039,633, "2F2FD3", 500, hwnd) Then // vpn 結束校驗
				Goto wall
			End If
		End If
		
		Rem time
		Call backHome(hwndChild,hwnd)
		
		Call click(67, 100, hwndChild)// setting
		If threePointCheck_respond(112,557, "889600", 224,702, "222222", 325,998, "CECECE", hwnd) Then // 設定的第一個畫面
			Call corruptRecovery(hwndChild, hwnd)
			vpnCounter = 0
			Goto start
		End If
		
		
		Call click(65, 100, hwndChild) // time & date
		
		If threePointCheck_respond(306,264, "737373", 197,253, "848484", 174,253, "7D7D7D", hwnd) Then // 設定日期的第一個畫面
			Call corruptRecovery(hwndChild, hwnd)
			vpnCounter = 0
			Goto start
		End If
		
		If threePointCheck(1741,226, "ECECEC",1746,242, "ECECEC", 1774,232, "B9B9B9", 100, hwnd)  Then // 檢查自動設定日期是否處於關閉狀態
			Call click(68, 100, hwndChild)
			Delay 300
		End If
		
		Call click(65, 300, hwndChild)// set date
		
		If threePointCheck_respond(601,590, "889600", 835,318, "212121", 1358,320, "212121", hwnd) Then // 檢查是否處於日期設定彈窗
			Call click(69, 0, hwndChild)
			Goto time
		End If
		
		
		Call click(70, 100, hwndChild) // 點擊年分
		
		Call click(66, 300, hwndChild) //previous day
		
		Call click(67, 300, hwndChild) // yes
		
		If threePointCheck_respond(439,131, "383226", 774,240, "FAFAFA", 1599,147, "383226", hwnd) Then // 檢查是否成功確認更改日期
			Call corruptRecovery(hwndChild, hwnd)
			vpnCounter = 0
			Goto start
		End If
		
		Delay 100
		Call backHome(hwndChild,hwnd)
		
		Call click(65, 100, hwndChild) // cat
		
		If threePointCheck_respond(816,707, "FFFFFF", 930,698, "4545C9", 1072,698, "40C6D7", hwnd) Then // 喵力達
			Call corruptRecovery(hwndChild, hwnd)
			vpnCounter = 0
			Goto start
		End If
		
		Call backHome(hwndChild, hwnd)
		
		
		Call click(67, 100, hwndChild)// setting
		If threePointCheck_respond(112,557, "889600", 224,702, "222222", 325,998, "CECECE", hwnd) Then // 設定的第一個畫面
			Call corruptRecovery(hwndChild, hwnd)
			vpnCounter = 0
			Goto start
		End If
		
		
		Call click(65, 100, hwndChild) // time & date
		
		If threePointCheck_respond(306,264, "737373", 197,253, "848484", 174,253, "7D7D7D", hwnd) Then // 設定日期的第一個畫面
			Call corruptRecovery(hwndChild, hwnd)
			vpnCounter = 0
			Goto start
		End If
		
		If threePointCheck_respond(306,264, "737373", 197,253, "848484", 174,253, "7D7D7D", hwnd) Then // 設定日期的第一個畫面
			Call corruptRecovery(hwndChild, hwnd)
			vpnCounter = 0
			Goto start
		End If
		
		Call click(68, 100, hwndChild) // auto time & date
		Call click(68, 200, hwndChild) // auto time & date
		
		If threePointCheck_respond(439,131, "383226", 774,240, "FAFAFA", 1599,147, "383226", hwnd) Then // 檢查是否成功確認更改日期
			Call corruptRecovery(hwndChild, hwnd)
			vpnCounter = 0
			Goto start
		End If
		
		Delay 100
		Call backHome(hwndChild,hwnd)
		
		Call click(65, 100, hwndChild)// cat
		
		Delay 300
		i = 0
		While threePointCheck(1393,138, "00C2FF", 1205,202, "FFFFFF", 680,219, "4F4F4F", 50, hwnd)//領取獎勵
			Call click(68, 0, hwndChild)// white
			
			If threePointCheck(532,558, "4FF9FF", 533,537, "3123FF", 566,542 , "2073F2", 0, hwnd) = False Then // 閃退
				Call corruptRecovery(hwndChild, hwnd)
				vpnCounter = 0
				Goto start
			End If
			
			If threePointCheck(816,707, "FFFFFF", 930,698, "4545C9", 1072,698, "40C6D7", 0, hwnd) = False Then // 喵力達(即將閃退)
				vpnCounter = vpnMAX
				Goto start
			End If
		
			If i >= 50 Then 
				Call corruptRecovery(hwndChild, hwnd)
				vpnCounter = 0
				Goto start
			End If
			i = i + 1
		Wend
		
		i = 0
		While threePointCheck(1714,166, "FFFFFF", 1777,172, "E2E2E2", 1717,206, "FFFFFF", 50, hwnd) // 換裝
			Call click(69, 0, hwndChild)// 領取獎勵
			
			If i >= 50 Then 
				Call corruptRecovery(hwndChild, hwnd)
				vpnCounter = 0
				Goto start
			End If
			i = i + 1
		Wend
		
		Rem restart11
		If vpnCounter = vpnMAX Then 
			Rem wall3
			Rem wall4
		
			Call backHome(hwndChild,hwnd)
			
			Call click(66, 0, hwndChild) // vpn
			
			If threePointCheck(554,132, "F9CA90", 551,424, "FAFAFA", 481,970, "F5A542", 500, hwnd) Then // vpn 初始校驗
				Goto wall3
			End If
			
			Call click(66, 0, hwndChild)
			
			If threePointCheck(848,265, "53C800", 852,332, "53C800", 1021,336, "53C800", 500, hwnd) Then // vpn 結束校驗
				Goto wall4
			End If
			
			Call backHome(hwndChild,hwnd)
			
			Call click(65, 0, hwndChild)
			
			vpnCounter = 0
			Delay 500
		End If

	Wend
End Function

Sub thread1
	Call main("gugu", 5, 5)
End Sub

Sub thread2
	Call main("SOP", 5, 4)
End Sub

Sub thread3
	Call main("jason", 5, 5)
End Sub


BeginThread thread1
BeginThread thread2
BeginThread thread3
Call main("oreo", 5, 5)
