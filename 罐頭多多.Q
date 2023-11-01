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
MacroID=266428d5-695c-4a50-8169-9be8f58e7852
Description=罐頭多多_oreo
Enable=1
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
	Delay 40
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

Function backHome(hwndChild, hwnd)
	i = 0
 	While threePointCheck(563, 540, "2E7CF4", 779, 509, "ADA69A", 828, 525, "F0EEEC", 0, hwnd)
		Call home(hwndChild, 0)
		i = i + 1
		
		If i > 5 Then 
			Goto endhome
		End If
		
		Delay 100
	Wend
	
	Delay 100
	Rem endhome
	
End Function

Function corruptRecovery(hwndChild, hwnd)
	deadline = 0

	Rem e1
	Rem e2
	Rem e3
	
	deadline = deadline + 1
	
	If deadline = 2 Then 
		Call click(116, 1500, hwndChild) // restart android
		Delay 30000 // wait 30 seconds to restart
		deadline = 0
		Call click(187, 1500, hwndChild)// click off advertisement
		Delay 1000
	End If
	
	Call backHome(hwndChild, hwnd) // at home page
	
	Call click(115, 0, hwndChild) // clean current mission

	
	Call click(67, 1000, hwndChild) // press setting
	
	If threePointCheck(830, 562, "ACA499", 565, 541, "2477F3", 525, 535, "3123FF", 1000, hwnd) = False Then 
	    // check it is at setting or not
		Goto e3
	End If
	
	For 4
		Call click(114, 1000, hwndChild) // 設定下滑到固定位置
	Next
	
	Call click(71, 1000, hwndChild)// 點擊系統
	Call click(187, 1000, hwndChild) // 點擊時間與日期
	
	If threePointCheck(300,117, "7F8C0F", 879,120, "F5F5F5", 1372,106, "F5F5F5", 600, hwnd) Then // 設定 初始校驗
		Goto e1
	End If
	
	Call click(68, 300, hwndChild) // auto time & date
	Call click(68, 300, hwndChild) // auto time & date
	
	Rem wall1
	Rem wall2
	
	Call backHome(hwndChild, hwnd)
	
	Call click(66, 0, hwndChild)
	
	If threePointCheck(493,124, "F9CA90", 521,377, "FAFAFA", 456,997, "F5A542", 700, hwnd) Then // vpn 初始校驗( no root 上藍、中白、下淺藍 )
		Goto wall1
	End If
	
	Call click(67, 0, hwndChild)
	
	Call click(66, 300, hwndChild)
	
	If threePointCheck(840,317, "53C800", 921,240, "53C800", 1033,358, "53C800", 700, hwnd) Then // vpn 結束校驗
		Goto wall2
	End If
	
	Call backHome(hwndChild, hwnd)
	
	Call click(65, 0, hwndChild)
	
	For 5
		Call click(65, 300, hwndChild)
	Next
	
	i = 0
	While threePointCheck(1607,942, "00C1FF", 1645,961, "FFFFFF", 1783,961, "00BFFD", 50, hwnd)  //skip
		If i >= 100 Then 
			Goto e2
		End If
		i = i + 1
	Wend
		
	
	Call click(73, 0, hwndChild) // 按skip
	
	i = 0
	While threePointCheck(347,710, "000000", 364,772, "43C1DA", 347,753, "226495", 50, hwnd)//加碼多多
	  	Call click(65, 0, hwndChild)
	  	Call click(71, 10, hwndChild)
	  	If threePointCheck(1579,171, "008FC8", 1586,122, "FFFFFF", 1526,114, "00B9F5", 0, hwnd) = False Then 
	  		Call click(69, 100, hwndChild)
	  	End If
	  	If threePointCheck(1190,781, "00C1FF", 1329,774, "00C1FF", 1301,811, "F6F6F6", 0, hwnd) = False Then 
	  		Call click(188, 100, hwndChild)
	  	End If
	  	If threePointCheck(630,826, "00C1FF", 1059,836, "00C1FF", 857,867, "FFFFFF", 0, hwnd) = False Then 
	  		Call click(191, 100, hwndChild)
	  	End If
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
        If threePointCheck(941,192, "BAB2A0", 918,216, "DACEB2", 968,199, "B9B19F", 0, hwnd) = False Then
        	currentLevel = 2 // 銀(check)
        Elseif threePointCheck(912,216, "86F6A7", 964,195, "F2C8A9", 950,213, "E99DE9", 0, hwnd) = False Then
        	currentLevel = 4 // 傳說(check)
        Elseif threePointCheck(942,194, "FFFFFF", 920,198, "FFFFFF", 969,217, "FFFFFF", 0, hwnd) = False Then
        	currentLevel = 0 // 白(check)
        Elseif threePointCheck(938,193, "2467CC", 970,199, "4566BA", 911,213, "4567BC", 0, hwnd) = False Then
        	currentLevel = 1 // 銅(check)
        Else 
        	currentLevel = 3 // 金
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
    
    i = 0
    While threePointCheck(633,716, "00C1FF", 825,743, "00BEFB", 720,760, "FFFFFF", 400, hwnd) // 判斷是否出現離隊確認彈窗
    	Call click(72, 0, hwndChild)// 離隊
    	i = i + 1
    	If i = 5 Then 
    			Goto endFunction
    	End If
    Wend
    
    i = 0
    While threePointCheck(1735,176, "42CFFF", 1716,162, "FFFFFF", 1779,175, "E2E2E2", 300, hwnd) // 判斷是否回到加碼多多原始頁面
    	Call click(67, 0, hwndChild)// 是
    	i = i + 1
    	If i = 10 Then 
    		Goto endFunction
    	End If
    Wend
    
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
		
		//If threePointCheck(537,551, "889600", 631,556, "212121", 551,654, "8F9C0E", 0, hwnd) = False Then // 桌面閃退
			//Call click(187, 0, hwndChild)// 重啟桌面
			//Delay 2000
			//Goto start
		//End If
		
		vpnCounter = vpnCounter + 1
		
		Call click(68, 0, hwndChild)// white
		
		If threePointCheck(1743,182, "42CFFF", 1724,164, "FFFFFF", 1763,222, "000000", 300, hwnd) = False Then // 判斷是否在加碼多多的畫面(換裝)
			Call corruptRecovery(hwndChild, hwnd)
			vpnCounter = 0
			Goto start
		End If
		
		If threePointCheck(823,699, "DB910A", 940,688, "FFFFFF", 1071,698, "45D5E0", 0, hwnd) = False Then // 已經開始(喵力達)
			Goto skip
		End If
		
		i = 0
		While threePointCheck(1022,683, "00B9F6", 1083,660, "000000", 1192,687, "FFFFFF", 0, hwnd) // 貓咪 start校驗(6小時深度探險按鈕)
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
		While threePointCheck(623,780, "009BD6", 639,720, "00C1FF", 748,758, "05020B", 0, hwnd) // 出現是否出發前一直點深度探險(是)
			If i Mod 3 = 0 Then
				Call click(66, 0, hwndChild)// 點深度探險
			End If
			
			i = i + 1
			
			If i > 15 Then 
				Call corruptRecovery(hwndChild, hwnd)
				vpnCounter = 0
				Goto start
			End If
			
			If threePointCheck(537,598 , "1B2224", 783,514, "FEFEFE", 1346,490, "233338", 200, hwnd) = False Then // 滿員(暫時判不了)
				min = keepLargest(hwndChild, hwnd, max, min)
				vpnCounter = vpnCounter - 1
				Goto start
			End If
		Wend
	
		i = 0
		While threePointCheck(629,718, "00C1FF", 641,785, "0096D0", 789,736, "00C1FF", 200, hwnd) = False // 如果確認出發前的彈窗還沒消失，就一直點確認出發(是)
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
		While threePointCheck(821,697, "D88903", 945,698, "1F982A", 1065,699, "0E1DB0", 0, hwnd) // 判斷是否已經出發去探險
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
			
			If threePointCheck(493,124, "F9CA90", 521,377, "FAFAFA", 456,997, "F5A542", 500, hwnd) Then // vpn 初始校驗( no root 上藍、中白、下淺藍 )
				Goto wall
			End If
			
			Call click(65, 0, hwndChild) // vpn start
			
			If threePointCheck(1040,651, "2F2FD3", 849,634, "2F2FD3", 844,704, "2F2FD3", 500, hwnd) Then // vpn 結束校驗( 停止的紅色 )
				Goto wall
			End If
		End If
		
		Rem time
		Call backHome(hwndChild,hwnd)
		
		Call click(67, 100, hwndChild)// setting
		If threePointCheck_respond(118,945, "757575", 135,857, "E8731A", 94,712, "C11150", hwnd) Then // 設定的第一個畫面
			Call corruptRecovery(hwndChild, hwnd)
			vpnCounter = 0
			Goto start
		End If
		
		Call click(71, 100, hwndChild) // system
		
		If threePointCheck_respond(226,122, "85911B", 115,601, "737373", 196,626, "787878", hwnd) Then // 設定的第二個畫面
			Call corruptRecovery(hwndChild, hwnd)
			vpnCounter = 0
			Goto start
		End If
		
		Call click(187, 100, hwndChild) // time & date
		
		If threePointCheck_respond(279,118, "798603", 188,220, "313131", 302,254, "747474", hwnd) Then // 設定日期的第一個畫面
			Call corruptRecovery(hwndChild, hwnd)
			vpnCounter = 0
			Goto start
		End If
		
		If threePointCheck(1748,231, "ECECEC",1774,232, "B9B9B9", 1746,245, "ECECEC", 100, hwnd)  Then // 檢查自動設定日期是否處於關閉狀態
			Call click(68, 100, hwndChild)
			Delay 300
		End If
		
		Call click(66, 300, hwndChild)// set date
		
		If threePointCheck_respond(573,666, "778500", 819,741, "FFFFFF", 1360,775, "A1AB4F", hwnd) Then // 檢查是否處於日期設定彈窗
			Call click(69, 0, hwndChild)
			Goto time
		End If
		
		
		Call click(70, 100, hwndChild) // 點擊年分
		
		Call click(66, 300, hwndChild) //previous day
		
		Call click(67, 300, hwndChild) // yes
		
		If threePointCheck_respond(448,125, "F5F5F5", 867,128, "F5F5F5", 1520,144, "F5F5F5", hwnd) Then // 檢查是否成功確認更改日期
			Call corruptRecovery(hwndChild, hwnd)
			vpnCounter = 0
			Goto start
		End If
		
		Delay 100
		Call backHome(hwndChild,hwnd)
		
		Call click(65, 100, hwndChild) // cat

		If threePointCheck_respond(823,699, "DB910A", 940,688, "FFFFFF", 1071,698, "45D5E0", hwnd) Then // 喵力達
			Call corruptRecovery(hwndChild, hwnd)
			vpnCounter = 0
			Goto start
		End If
		
		Delay 300
		
		Call backHome(hwndChild, hwnd)
		
		Call click(67, 100, hwndChild)// setting
		If threePointCheck_respond(118,945, "757575", 135,857, "E8731A", 94,712, "C11150", hwnd) Then // 設定的第一個畫面
			Call corruptRecovery(hwndChild, hwnd)
			vpnCounter = 0
			Goto start
		End If
		
		Call click(71, 100, hwndChild) // system
		
		If threePointCheck_respond(226,122, "85911B", 115,601, "737373", 196,626, "787878", hwnd) Then // 設定的第二個畫面
			Call corruptRecovery(hwndChild, hwnd)
			vpnCounter = 0
			Goto start
		End If
		
		Call click(187, 100, hwndChild) // time & date
		
		If threePointCheck_respond(279,118, "798603", 188,220, "313131", 302,254, "747474", hwnd) Then // 設定日期的第一個畫面
			Call corruptRecovery(hwndChild, hwnd)
			vpnCounter = 0
			Goto start
		End If
		
		Call click(68, 100, hwndChild) // auto time & date
		Call click(68, 200, hwndChild) // auto time & date
		
		If threePointCheck_respond(448,125, "F5F5F5", 867,128, "F5F5F5", 1520,144, "F5F5F5", hwnd) Then // 檢查是否成功確認更改日期
			Call corruptRecovery(hwndChild, hwnd)
			vpnCounter = 0
			Goto start
		End If
		
		Delay 100
		Call backHome(hwndChild,hwnd)
		
		Call click(65, 100, hwndChild)// cat
		
		Delay 300
		i = 0
		While threePointCheck(1408,163, "00BAF7", 1626,185, "009BD4", 1512,148, "000000", 50, hwnd)//領取獎勵
			Call click(68, 0, hwndChild)// white
			
			If threePointCheck(532,558, "4FF9FF", 533,537, "3123FF", 566,542 , "2073F2", 0, hwnd) = False Then // 閃退
				Call corruptRecovery(hwndChild, hwnd)
				vpnCounter = 0
				Goto start
			End If
			
			If threePointCheck(823,699, "DB910A", 940,688, "FFFFFF", 1071,698, "45D5E0", 200, hwnd) = False Then // 喵力達(即將閃退)
				vpnCounter = vpnMAX
				Goto restart11
			End If
		
			If i >= 50 Then 
				Call corruptRecovery(hwndChild, hwnd)
				vpnCounter = 0
				Goto start
			End If
			i = i + 1
		Wend
		
		i = 0
		While threePointCheck(1720,162, "FFFFFF", 1731,178, "42CEFF", 1746,199, "42CEFE", 50, hwnd) // 換裝
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
			
			If threePointCheck(493,124, "F9CA90", 521,377, "FAFAFA", 456,997, "F5A542", 500, hwnd) Then // 確認進入vpn app( no root 上藍、中白、下淺藍 )
				Goto wall3
			End If
			
			Call click(66, 0, hwndChild)
			
			If threePointCheck(840,317, "53C800", 921,240, "53C800", 1033,358, "53C800", 500, hwnd) Then // vpn 結束校驗
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
	Call main("gugu", 5, 1)
End Sub

Sub thread2
	Call main("SOP", 5, 5)
End Sub

Sub thread3
	Call main("jason", 5, 5)
End Sub


Call main("oreo", 5, 3)