# -*- coding: utf-8 -*-
import os
from kaki.app import App
from kivy.factory import Factory
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.config import Config

Config.set('graphics', 'width', '657')
Config.set('graphics', 'height', '805')
Config.write()

#from kivy.app import App
Window.size = (657,805)

class Live(App,MDApp):


      CLASSES = {
          "UI": "main"
      }
      KV_FILES = {
          os.path.join(os.getcwd(), "tap.kv")
      }
      AUTORELOADER_PATHS = [
          (".", {"recursive": True}),
      ]

      def build_app(self):

          return Factory.UI()
         # pass


if __name__=="__main__":
    Live().run()
