from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime
import random

Builder.load_file("design.kv")


class LoginScreen(Screen):

    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login(self, uname, pword):
        self.manager.transition.direction = "left"
        try:
            with open("users.json") as file:
                users = json.load(file)

            if users[uname]["password"] == pword:
                self.manager.current = "login_screen_success"
            else:
                self.ids.login_wrong.text = "Wrong username or password"

        except KeyError:
            self.ids.login_wrong.text = "Wrong username or password"


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


class MainApp(App):

    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
