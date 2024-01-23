import ctypes
import time
import pyautogui
import subprocess
import pygetwindow as gw

#ctypes library with the following command has the power to block user's acess to keyboard and mouse
ctypes.windll.user32.BlockInput(True)

cleanmgr_path = r'C:\Windows\System32\cleanmgr.exe'

Command = [cleanmgr_path, '/lowdisk']

# open the cleanmgr.exe
subprocess.Popen(Command)

# await until it opens
time.sleep(10)

window_title = 'Limpeza de Disco'

cleanmgr_window = gw.getWindowsWithTitle(window_title)

# Check if the window was found
if cleanmgr_window:
    cleanmgr_window = cleanmgr_window[0]
    
    # Move the mouse to it's center (also aplicable to navigators tabs like google chrome or firefox for example)
    window_center_x = cleanmgr_window.left + cleanmgr_window.width / 2
    window_center_y = cleanmgr_window.top + cleanmgr_window.height / 2

    pyautogui.moveTo(window_center_x, window_center_y)

    button_x   = window_center_x - 155
    button_y   = window_center_y - 103

    button_x2  = window_center_x - 155
    button_y2  = window_center_y - 84

    button_x3  = window_center_x - 155
    button_y3  = window_center_y - 67

    button_x4  = window_center_x - 155
    button_y4  = window_center_y - 47

    button_x5  = window_center_x - 155
    button_y5  = window_center_y - 29

    button_x6  = window_center_x - 155
    button_y6  = window_center_y - 7

    button_x7  = window_center_x - 155
    button_y7  = window_center_y + 3

    button_x8  = window_center_x - 155
    button_y8  = window_center_y + 23

    button_x9  = window_center_x - 155
    button_y9  = window_center_y + 43

    button_x10  = window_center_x - 155
    button_x10  = window_center_x + 63

    button_y11 = window_center_y - 85
    button_x11 = window_center_x + 83

    button_x12 = window_center_x - 155
    button_y12 = window_center_y + 103

    button_okx = window_center_x + 80
    button_oky = window_center_y + 210



    # Move the cursor to "OK" button
    pyautogui.moveTo(button_x, button_y, duration=0)

    pyautogui.doubleClick ()
    pyautogui.click()

    pyautogui.moveTo (button_x2, button_y2, duration=0)

    pyautogui.doubleClick ()
    pyautogui.click ()
   
     
    pyautogui.moveTo (button_x3, button_y3, duration=0)

    pyautogui.doubleClick ()
    pyautogui.click ()
    

    pyautogui.moveTo (button_x4, button_y4, duration=0)

    pyautogui.doubleClick ()
    pyautogui.click ()
   
    # Scroll down the mouse in the cleanmgr.exe window so you can check every box
    
    pyautogui.scroll(-220)  # 10 units down

    # When scroll down the mouse the button_y position changes to:
    # button_y(X) = button_y(x) - button_y(x) - 1
     
    pyautogui.moveTo(button_x4, button_y3, duration=0)
    pyautogui.click ()


    pyautogui.moveTo (button_x5, button_y4, duration=0)

    pyautogui.doubleClick ()
    pyautogui.click ()
    

    pyautogui.moveTo (button_x6, button_y5, duration=0)

    pyautogui.doubleClick ()
    pyautogui.click ()
    

    pyautogui.moveTo (button_x7, button_y6, duration=0)

    pyautogui.doubleClick ()
    pyautogui.click ()
    

    pyautogui.moveTo (button_okx, button_oky, duration=0)
    pyautogui.click ()


pyautogui.moveTo (972, 534, duration = 0)
pyautogui.click ()

time.sleep(20)

pyautogui.moveTo (1084, 576)
pyautogui.click ()


window_title2 = 'Notificação de espaço em disco'

cleanmgr_window2 = gw.getWindowsWithTitle(window_title2)

window_title2 = 'Notificação de espaço em disco'

cleanmgr_window2 = gw.getWindowsWithTitle(window_title2)

if cleanmgr_window2:
    cleanmgr_window2 = cleanmgr_window2[0]

    window_center_x2 = cleanmgr_window2.left + cleanmgr_window2.width / 2
    window_center_y2 = cleanmgr_window2.top + cleanmgr_window2.height / 2

    pyautogui.moveTo(window_center_x, window_center_y)  

    pyautogui.moveTo (1087, 575, duration=0)

    pyautogui.click ()

else :
     print ("Janela de notificação de espaço em disco não encontrada") 
   

# Aguardar alguns segundos
time.sleep(1)

# Desbloquear entrada do mouse e teclado
ctypes.windll.user32.BlockInput(False)
exit
