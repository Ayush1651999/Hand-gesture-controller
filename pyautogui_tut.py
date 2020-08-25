import pyautogui 
# print(pyautogui.size())
# pyautogui.moveTo(500, 500, duration = 1.414)
# pyautogui.hotkey("alt", "3")
# pyautogui.hotkey("winleft", "l")
# pyautogui.moveRel(500, 0, duration = 1)
# pyautogui.press('enter')
# pyautogui.press('winleft')

# pyautogui.keyDown('alt')
# pyautogui.keyDown('shift') 
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.keyUp('shift')
# pyautogui.keyUp('alt')

# pyautogui.keyDown('ctrlleft')
# pyautogui.keyUp('ctrlleft')

# def minimize_all():
# 	pyautogui.keyDown('winleft')
# 	pyautogui.press('m')
# 	pyautogui.keyUp('winleft')


def minimize_all():
	pyautogui.keyDown('ctrlleft')
	pyautogui.keyDown('winleft')
	pyautogui.press('d')
	pyautogui.keyUp('winleft')
	pyautogui.keyUp('ctrlleft')

def alt_tab():
	pyautogui.keyDown('altleft')
	pyautogui.press('tab')
	pyautogui.keyUp('altleft')

def alt_shift_tab():
	pyautogui.keyDown('altleft')
	pyautogui.keyDown('shiftleft')
	pyautogui.press('tab')
	pyautogui.keyUp('shiftleft')
	pyautogui.keyUp('altleft')	

alt_tab()
alt_tab()