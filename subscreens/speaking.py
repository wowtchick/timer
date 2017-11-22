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


class Speaking(Screen):
    """Screen class body"""
    self_timedelta = timedelta()
    event = None
    is_tick = False
    sound = SoundLoader.load('Bepp-beep.mp3')

    def start_stop_thinking(self):
        """Start stop timer for thinking count"""
        if self.is_tick:
            self.cancel()
        else:
            self.ids["time_l"].text = "00:01:00"
            self.self_timedelta = timedelta(minutes=1)
            self.event = Clock.schedule_interval(self.tick, 1)
            self.is_tick = True

    def start_stop_speaking(self):
        """Start stop timer for speaking count"""
        if self.is_tick:
            self.cancel()
        else:
            self.ids["time_l"].text = "00:02:00"
            self.self_timedelta = timedelta(minutes=2)
            self.event = Clock.schedule_interval(self.tick, 1)
            self.is_tick = True

    def tick(self, passed_timedelta):
        """Handle time tick
        passed_timedelta is needed by Clock.schedule_interval
        """
        self.self_timedelta = self.self_timedelta - timedelta(seconds=1)
        if self.self_timedelta.seconds == 0:
            self.cancel()
            if self.sound:
                self.sound.play()
        self.ids["time_l"].text = str(self.self_timedelta)

    def cancel(self):
        """Cancel timer"""
        if self.event:
            self.event.cancel()
            self.event = None
            self.is_tick = False

    def reset(self):
        """Reset the timer"""
        self.cancel()
        self.ids["time_l"].text = "00:00:00"
