import pyautogui
import time
import clipboard
def write():
      pyautogui.click(335,485)

      pyautogui.drag(539,549)

      pyautogui.hotkey('ctrl', 'c', interval = 0.15)
      
      text = clipboard.paste()
      
      text = text.replace('␣',' ')

      text = text.replace('↵',' ')
      
      pyautogui.write(text)
write()
