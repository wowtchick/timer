"""IELTS timer program main module

Copyright (c) 2017 Vladimir Kortishko

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from subscreens.listening import Listening
from subscreens.reading import Reading
from subscreens.speaking import Speaking


class ScreenManagement(ScreenManager):
    """Screen manager class to load screens."""
    pass


class MainScreen(Screen):
    """The main screen, essential in the main.kv"""
    pass


class MainApp(App):
    """Main class body"""
    inner_screen_manager = None

    def build(self):
        """Loading and building screens"""
        Builder.load_file("subscreens/listening.kv")
        Builder.load_file("subscreens/reading.kv")
        Builder.load_file("subscreens/speaking.kv")
        self.inner_screen_manager = ScreenManager()
        self.inner_screen_manager.add_widget(MainScreen())
        self.inner_screen_manager.add_widget(Listening())
        self.inner_screen_manager.add_widget(Reading())
        self.inner_screen_manager.add_widget(Speaking())
        return self.inner_screen_manager


if __name__ in ("__main__", "__android__"):
    MainApp().run()
