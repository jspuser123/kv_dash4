from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window

#from kivy.config import Config

#Config.set('graphics', 'width', '1920')
#Config.set('graphics', 'height', '900')
#Config.write()

#from kivy.app import App
Window.size = (1920,900)

KV = '''
<CommonComponent>
   


<MobileView>
    MDCard:
        md_bg_color:"yellow"
        spacing:10
        padding:10
    
       


<TabletView>
    ScrollView:

        BoxLayout:
            orientation: 'vertical'

            padding: 15
            spacing: 15
            size_hint: 1, None
            height: self.minimum_height


            MDCard:
                size_hint_y: None
                height: 500
                MDRaisedButton:

                    pos_hint: {'center_x':0.5}
                    md_bg_color: 1,0,0,1
                    text: "Submit"
            MDCard:
                size_hint_y: None
                height: 500
                MDRaisedButton:

                    pos_hint: {'center_x':0.5}
                    md_bg_color: 1,0,0,1
                    text: "Submit"
            MDCard:
                size_hint_y: None
                height: 500
                MDRaisedButton:

                    pos_hint: {'center_x':0.5}
                    md_bg_color: 1,0,0,1
                    text: "Submit"
            MDCard:
                size_hint_y: None
                height: 500
                MDRaisedButton:

                    pos_hint: {'center_x':0.5}
                    md_bg_color: 1,0,0,1
                    text: "Submit" 
    
    
<DesktopView>
   
    md_bg_color:"#1A2035"
    AnchorLayout:
        md_bg_color: "#1A2035"
        anchor_x:'right'
        anchor_y:'top'

        MDCard:
            spacing:10
            padding:10
            md_bg_color:"#1A2035"
            elevation: 1
            radius:0,0,0,0
            size_hint_y:.06
            size_hint_x:.95
            MDScreen:

                Label:
                    text:"VEE YES SOFTWARES"
                    pos_hint: {"center_x": .054,"center_y":.6}
                    font_size:20
                MDRaisedButton:

                    pos_hint: {'center_x':.81}
                    md_bg_color: "#1A2035"
                    text: "Domestic"
                    on_press:nav_drawer.set_state('toggle')
                MDRaisedButton:

                    pos_hint: {'center_x':.85}
                    md_bg_color: "#1A2035"
                    text: "Export"
                    on_press:nav_drawer.set_state('toggle')
                MDRaisedButton:

                    pos_hint: {'center_x':.89}
                    md_bg_color: "#1A2035"
                    text: "Payroll"
                    on_press:nav_drawer.set_state('toggle')
                Label:
                    text:"23-22"
                    pos_hint: {'center_x':.93}

                    md_bg_color: "white"
                MDIconButton:
                    icon: "email"
                    theme_text_color: "Custom"
                    text_color: "white"
                    pos_hint: {'center_x':.95}
                MDIconButton:
                    icon: "cloud-download"
                    theme_text_color: "Custom"
                    text_color: "white"
                    pos_hint: {'center_x':.97}
                MDIconButton:
                    icon: "account-circle"
                    theme_text_color: "Custom"
                    text_color: "white"
                    pos_hint: {'center_x':.99}







    ScrollView:
        size_hint_y:.87
        size_hint_x:.96
        pos_hint:{'x':.05,'y':.05}
        BoxLayout:
            orientation: 'vertical'
            padding: 15
            spacing: 15
            size_hint: 1, None
            height: self.minimum_height
                                                                      ####irow
            MDCard:
                size_hint_y: None
                height: 500
                md_bg_color:"#1A2035"
                orientation:'vertical'
                MDCard:
                    md_bg_color:"#1A2035"
                    size_hint_y:None
                    MDScreen:

                        Label:
                            text:"Welcome back, jagan!"
                            pos_hint: {"center_x": .045,"center_y":.6}
                            font_size:17
                        Label:
                            text:"Yesterday I was clever, so I wanted to change the world. Today I am wise, so I am changing myself."
                            pos_hint: {"center_x":.183,"center_y":.3}
                                                                            ##############2row
                MDCard:
                    md_bg_color:"#1A2035"
                    spacing:10
                    padding:10

                   # orientation:'vertical'
                    size_hint_y:None

                    MDCard:
                        md_bg_color:"#1572E8"
                        spacing:0
                        padding:0
                        #size_hint_y:.7
                    MDCard:
                        md_bg_color:"#48ABF7"
                        spacing:0
                        padding:0
                        #size_hint_y:.7
                    MDCard:
                        md_bg_color:"#31CE36"
                        spacing:0
                        padding:0
                        #size_hint_y:.7
                    MDCard:
                        md_bg_color:"#6861CE"
                        spacing:0
                        padding:0
                       # size_hint_y:.7
                                                                    ##############3row
                MDCard:
                    md_bg_color:"#1A2035"
                    spacing:10
                    padding:10
                   # orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'


                MDCard:
                    md_bg_color:"#1A2035"
                    spacing:10
                    padding:10
                   # orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'

                                                                        ###########4 row
            MDCard:
                size_hint_y: None
                height: 500
                orientation:'vertical'
                md_bg_color:"#1A2035"
                MDCard:
                    spacing:10
                    padding:10
                    md_bg_color:"#1A2035"
                    #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"##202940"
                        #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'
                        MDRaisedButton:

                            pos_hint: {'center_x':0.5}
                            md_bg_color: 1,0,0,1
                            text: "Submit"
                            on_press:nav_drawer.set_state('toggle')

                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'


                MDCard:
                    spacing:10
                    padding:10
                    md_bg_color:"#1A2035"
                    #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"##202940"
                        #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'

                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'
                MDCard:
                    spacing:10
                    padding:10
                    md_bg_color:"#1A2035"
                    #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"##202940"
                        #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'
                MDCard:
                    spacing:10
                    padding:10
                    md_bg_color:"#1A2035"
                    #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"##202940"
                        #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#202940"
                        #orientation:'vertical'
                    MDCard:
                        spacing:10
                        padding:10
                        md_bg_color:"#1A2035"
                        #orientation:'vertical'


            MDCard:
                size_hint_y: None
                height: 300
                md_bg_color:"#1A2035"
                spacing:10
                padding:10
                MDCard:
                    spacing:10
                    padding:10
                    md_bg_color:"#202940"
                    #orientation:'vertical'
                MDCard:
                    spacing:10
                    padding:10
                    md_bg_color:"#202940"
                    #orientation:'vertical'

            MDCard:
                size_hint_y: None
                height: 500
                md_bg_color: 1,2,2,.3
                MDRaisedButton:

                    pos_hint: {'center_x':0.5}
                    md_bg_color: 1,0,0,1
                    text: "Submit"
                    on_press:nav_drawer.set_state('toggle')

    AnchorLayout:
        #md_bg_color: 0,23,2,23
        anchor_x:'left'
        anchor_y:'center'
        md_bg_color:"#1A2035"

        MDCard:
            spacing:0
            padding:0
            md_bg_color:"#1A2035"
            elevation: 1
            radius:0,0,0,0
            size_hint_y:1
            size_hint_x:.05
            MDScreen:
                MDIconButton:
                    icon: "dots-vertical"
                    theme_text_color: "Custom"
                    text_color: "white"
                    pos_hint: {'center_y':.95}
                MDIconButton:
                    icon: "account-circle"
                    theme_text_color: "Custom"
                    text_color: "white"
                    pos_hint: {'center_y':.9}
                MDIconButton:
                    icon: "pencil-box"
                    theme_text_color: "Custom"
                    text_color: "white"
                    pos_hint: {'center_y':.85}

                MDIconButton:
                    icon: "layers-triple"
                    theme_text_color: "Custom"
                    text_color: "white"
                    pos_hint: {'center_y':.8}
                MDIconButton:
                    icon: "book-open-variant"
                    theme_text_color: "Custom"
                    text_color: "white"
                    pos_hint: {'center_y':.75}
                MDIconButton:
                    icon: "cube"
                    theme_text_color: "Custom"
                    text_color: "white"
                    pos_hint: {'center_y':.7}
                MDIconButton:
                    icon: "gamepad-round-down"
                    theme_text_color: "Custom"
                    text_color: "white"
                    pos_hint: {'center_y':.65}
                MDIconButton:
                    icon: "flash-triangle"
                    theme_text_color: "Custom"
                    text_color: "white"
                    pos_hint: {'center_y':.6}

                MDIconButton:
                    icon: "store"
                    theme_text_color: "Custom"
                    text_color: "white"
                    pos_hint: {'center_y':.55}
                MDIconButton:
                    icon: "layers-triple-outline"
                    theme_text_color: "Custom"
                    text_color: "white"
                    pos_hint: {'center_y':.5}
                MDIconButton:
                    icon: "alpha-m"
                    theme_text_color: "Custom"
                    text_color: "white"
                    pos_hint: {'center_y':.45}
                MDIconButton:
                    icon: "store-cog"
                    theme_text_color: "Custom"
                    text_color: "white"
                    pos_hint: {'center_y':.4}
                MDIconButton:
                    icon: "database"
                    theme_text_color: "Custom"
                    text_color: "white"
                    pos_hint: {'center_y':.35}

                MDIconButton:
                    icon: "layers-triple"
                    theme_text_color: "Custom"
                    text_color: "white"
                    pos_hint: {'center_y':.3}
                MDIconButton:
                    icon: "ambulance"
                    theme_text_color: "Custom"
                    text_color: "white"
                    pos_hint: {'center_y':.25}
                MDIconButton:
                    icon: "cog"
                    theme_text_color: "Custom"
                    text_color: "white"
                    pos_hint: {'center_y':.2}
                MDIconButton:
                    icon: "chart-box"
                    theme_text_color: "Custom"
                    text_color: "white"
                    pos_hint: {'center_y':.15}





    MDNavigationLayout:
        MDNavigationDrawer:
            id: nav_drawer
            md_bg_color:"#1A2035"
            MDRaisedButton:

                text: "Submit"

ResponsiveView:
'''


class CommonComponent(MDScreen):
    pass


class MobileView(MDScreen):
    pass


class TabletView(MDScreen):
    pass


class DesktopView(MDScreen):
    pass


class ResponsiveView(MDResponsiveLayout, MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()
        self.desktop_view = DesktopView()


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()
