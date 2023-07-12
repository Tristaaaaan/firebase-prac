from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.app import MDApp

import requests
import json
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout


class ClickableTextField(MDRelativeLayout):
    password = StringProperty()


firebase_url = 'https://login-e4383-default-rtdb.asia-southeast1.firebasedatabase.app/.json'


class FirstWindow(Screen):

    Builder.load_file('firstwindow.kv')

    def login(self):
        password_text = self.ids.password.passw.text
        username_text = self.ids.username.text
        json_data = json.dumps(
            {"Username": username_text, "Password": password_text})

        res = requests.patch(url=firebase_url, json=json.loads(json_data))


class WindowManager(ScreenManager):
    pass


class rawApp(MDApp):

    def build(self):

        return WindowManager()


if __name__ == '__main__':
    rawApp().run()
