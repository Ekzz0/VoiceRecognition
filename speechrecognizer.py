import speech_recognition
import pyperclip
from pynput import keyboard
import pyautogui as pg
import time

def listen_command():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:

        r.pause_threshold = 0.5
        text = '0'
        print("Говори:")
        r.adjust_for_ambient_noise(source=mic, duration=0.5) # учет уровня шума
        audio = r.listen(source=mic)
        try:
            text = r.recognize_google(audio_data=audio, language='ru-RU').lower()
        except speech_recognition.UnknownValueError:
            return "Непонятная ошибка"
        return text


def start():
    pyperclip.copy(listen_command())
    print("из буфера:", pyperclip.paste())


def on_activate_i():
    print('Нажато сочетание клавиш: <ctrl>+i')


def exit():
    quit()

#ssssssssss
#Тестовая ветка ыыыыы
def press_buttons():
    pg.hotkey('enter')
    time.sleep(0.1)
    pg.hotkey('ctrl', 'v')
    time.sleep(0.1)
    pg.hotkey('enter')



with keyboard.GlobalHotKeys({
    '<shift>': start,
    '<tab>': exit}) as h:
    h.join()




