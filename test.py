from win32gui import GetWindowText, GetForegroundWindow
import time
from pynput import keyboard

def on_activate_i():
    time.sleep(1)
    print('Нажато сочетание клавиш: <ctrl>+i')


current_window = (GetWindowText(GetForegroundWindow()))
# desired_window_name = "Stopwatch" #Whatever the name of your window should be
time.sleep(3)
print(current_window)
if current_window[:10] == "- ArcheAge":
    print("Окно обнаружено")
    with keyboard.GlobalHotKeys({
        '<shift>': on_activate_i}) as h:
        h.join()

# #Infinite loops are dangerous.
# while True: #Don't rely on this line of code too much and make sure to adapt this to your project.
#     if current_window == desired_window_name:
#
#         with Listener(
#             on_press=on_press,
#             on_release=on_release) as listener:
#             listener.join()