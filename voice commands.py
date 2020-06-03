import speech_recognition as sr
import pyautogui
import time

def get_audio():
    r = sr.Recognizer()    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=2)
        said = ''
        said = r.recognize_google(audio)
    return said.lower()
try:
    while True:
        try:
            text=''
            text = get_audio()
            print(text)
            if 'increase' in text:
                pyautogui.hotkey('ctrl','up')
                time.sleep(0.3)
                pyautogui.hotkey('ctrl','up')
                time.sleep(0.3)
                pyautogui.hotkey('ctrl','up')
            elif 'down' in text:
                pyautogui.hotkey('ctrl','down')
                time.sleep(0.3)
                pyautogui.hotkey('ctrl','down')
                time.sleep(0.3)
                pyautogui.hotkey('ctrl','down')
            elif 'right' in text:
                pyautogui.hotkey('ctrl','right')
            elif 'left' in text:
                pyautogui.hotkey('ctrl','left')
            elif 'start' in text:
                pyautogui.hotkey('p')
            elif 'stop' in text:
                pyautogui.hotkey('p')
            else:
                print("noise")
        except Exception:
            continue
except KeyboardInterrupt:
    print('interrupted!')