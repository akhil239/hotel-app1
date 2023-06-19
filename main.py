import kivy
from kivy.uix.label import Label
from kivy.app import App



class Test(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "hi"

class Run(App):
    def build(self):
        return Test()
Run().run()
