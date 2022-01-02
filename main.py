from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json
from datetime import datetime
import random


Builder.load_file("design.kv")


class LoginScreen(Screen):

    def sign_up(self):
        self.manager.transition.direction = "left"
        self.manager.current = "sign_up_screen"

    def login(self, uname, pword):
        self.manager.transition.direction = "left"
        try:
            with open("users.json") as file:
                users = json.load(file)

            if users[uname]["password"] == pword:
                self.manager.current = "login_screen_success"
            else:
                self.ids.warning.text = "Wrong username or password"

        except KeyError:
            self.ids.warning.text = "Wrong username or password"

    def show_password(self):
        if self.ids.password.password:
            self.ids.password.password = False
            self.ids.show_password.text = "Hide Password"
        else:
            self.ids.password.password = True
            self.ids.show_password.text = "Show Password"

    def forgot_password(self):
        self.ids.warning.text = "Make a new account"


class RootWidget(ScreenManager):
    pass


class SignUpScreen(Screen):

    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)

        users[uname] = {"username": str(uname),
                        "password": str(pword),
                        "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

        with open("users.json", "w") as file:
            json.dump(users, file)
        self.manager.current = "sign_up_screen_success"


class SignUpScreenSuccess(Screen):

    def move_to_login_page(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"


class LoginScreenSuccess(Screen):

    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def show_quote(self, feeling):
        feeling = feeling.lower()
        if feeling == "happy":
            with open("quotes/happy.txt", encoding="utf-8") as file:
                quote = random.choice(file.readlines())
        elif feeling == "sad":
            with open("quotes/sad.txt", encoding="utf-8") as file:
                quote = random.choice(file.readlines())
        elif feeling == "unloved":
            with open("quotes/unloved.txt", encoding="utf-8") as file:
                quote = random.choice(file.readlines())
        else:
            quote = "You can only input happy, sad, or unloved"
        self.ids.quote_label.text = quote.strip()


class ImageButton(ButtonBehavior, Image, HoverBehavior):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
