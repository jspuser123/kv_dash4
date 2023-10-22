from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
import Desktop
import Tap
import Mobile
#from kivy.factory import Factory as F

#from kivy.config import Config

#Config.set('graphics', 'width', '1920')
#Config.set('graphics', 'height', '900')
#Config.write()

#from kivy.app import App
#Window.size = (1920,900)

##class UI(F.ScreenManager):
 #   def __init__(self, **kw):
  #      super().__init__(**kw)
   #     self.tap = Tap.TabletView()
    # Builder.load_file('load.kv')
     #Builder.load_file('F://js//tools//kaki-master//examples//livedemo//live//load.kv')
    #    pass




class ResponsiveView(MDResponsiveLayout, MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = Mobile.MobileView()
        self.tablet_view = Tap.TabletView()
        self.desktop_view = Desktop.DesktopView()



class Test(MDApp):
    def build(self):
       # return Builder.load_string(KV)
        return	ResponsiveView()


Test().run()