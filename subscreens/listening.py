"""IELTS timer program speaking module

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
from datetime import timedelta
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import Screen


class Listening(Screen):
    """Listening screen body"""
    sdt = timedelta(minutes=10)
    event = None
    is_tick = False
    sound = SoundLoader.load('Bepp-beep.mp3')

    def start_continue(self):
        """Handle start/continue button"""
        if self.is_tick:
            self.is_tick = False
            self.event.cancel()
        else:
            self.event = Clock.schedule_interval(self.tick, 1)
            self.is_tick = True

    def tick(self, __timedelta):
        """Handle time tick

        __timedelta is needed for Clock.schedule_interval"""
        self.sdt = self.sdt - timedelta(seconds=1)
        self.ids["time_l"].text = str(self.sdt)
        if self.sdt.seconds % 60 == 0:
            _minutes = self.sdt.seconds // 60
            sound = None
            if _minutes == 5:
                sound = SoundLoader.load("5mleft.flac")
            if _minutes == 1:
                sound = SoundLoader.load("1mleft.flac")
            if sound:
                sound.play()

        if self.sdt.seconds == 0:
            self.reset()
            self.sound = SoundLoader.load("Bepp-beep.mp3")
            self.sound.play()

    def reset(self):
        """Handle reset button click"""
        if self.event:
            self.event.cancel()
            self.event = None
            self.is_tick = False
            self.ids["time_l"].text = "00:10:00"
            self.sdt = timedelta(minutes=1)
