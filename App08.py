#App is base of any kivy application.
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class LoveStoryGame(ScreenManager):
    pass

class StartScreen(Screen):
    pass

class GameScreen(Screen):
    pass


class App08(App):
    def build(self):
        return LoveStoryGame()


if __name__ == '__main__':
    App08().run()
