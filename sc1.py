from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.label import MDLabel
from screens import screen_helper
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from kivy.uix.image import Image
from kivymd.uix.button import MDRaisedButton
Window.size=(350,600)
screen_helper = """
ScreenManager:
    MenuScreen
    LoginScreen
    SignupScreen
    SignupScreen1
    Workers_list
    Worker_profile
    checkout
<MenuScreen>
    name:"menu"
    MDLabel:
        text:"FARMA-DEMO"
        halign:'center'
        theme_text_color:'Primary'
        font_style:'H4'
        pos_hint:{'center_x':0.5,'center_y':0.7}
        theme_style:'Dark'
    MDRaisedButton:
        text:"LOGIN"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_press:root.manager.current='login'
    MDRaisedButton:
        text:"SIGN-UP"
        pos_hint:{'center_x':0.5,'center_y':0.4}
        on_press:root.manager.current='signup'


<LoginScreen>
    name:"login"
    MDLabel:
        text:"FARMA-LOGO"
        halign:"center"
        pos_hint:{'center_x':0.5,'center_y':0.6}
        font_style:'H4'

    MDTextField:
        hint_text:"Enter Username"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:300
    MDTextField:
        hint_text:"Enter Password"
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint_x:None
        width:300
    MDRaisedButton:
        text:"LOGIN"
        pos_hint:{'center_x':0.7,'center_y':0.2}
        on_press:root.manager.current='worker'
    MDRaisedButton:
        text:"BACK"
        pos_hint:{'center_x':0.2,'center_y':0.2}
        on_press:root.manager.current="menu"


<SignupScreen>
    name:"signup"
    MDLabel:
        text:"WELCOME TO SIGN-UP PAGE"
        halign:"center"
        pos_hint:{'center_x':0.5,'center_y':0.9}
        font_style:'H4'
        theme_text_color:'Primary'
    MDTextField:
        hint_text:"Enter Name"
        pos_hint:{'center_x':0.5,'center_y':0.7}
        size_hint_x:None
        width:300
    MDTextField:
        hint_text:"Enter Aadhar Number"
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        width:300
    MDTextField:
        hint_text:"Enter PhoneNumber"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:300
    MDTextField:
        hint_text:"Enter State"
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint_x:None
        width:300
    MDTextField:
        hint_text:"Enter City/Village"
        pos_hint:{'center_x':0.5,'center_y':0.3}
        size_hint_x:None
        width:300
    MDRaisedButton:
        text:"Next"
        pos_hint:{'center_x':0.7,'center_y':0.1}
        on_press:root.manager.current="signup1"
    MDRaisedButton:
        text:"BACK"
        pos_hint:{'center_x':0.2,'center_y':0.1}
        on_press:root.manager.current="menu"
<SignupScreen1>
    name:'signup1'
    MDLabel:
        text:"WELCOME TO SIGN-UP PAGE"
        halign:"center"
        pos_hint:{'center_x':0.5,'center_y':0.9}
        font_style:'H4'
        theme_text_color:'Primary'
    MDTextField:
        hint_text:"Enter User-Name"
        pos_hint:{'center_x':0.5,'center_y':0.7}
        size_hint_x:None
        width:300   
    MDTextField:
        hint_text:"Enter Password"
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        width:300
    MDTextField:
        hint_text:"Re-Enter Password"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:300
    MDRaisedButton:
        text:"SUBMIT"
        pos_hint:{'center_x':0.7,'center_y':0.3}
    MDRaisedButton:
        text:"BACK"
        pos_hint:{'center_x':0.2,'center_y':0.3}
        on_press:root.manager.current="signup"



<workers_list>
    name:'worker'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Demo'
                        elevation: 4
                        left_action_items: [['menu', lambda x: nav_draw.set_state('open')]]
                    MDCard:
                        size_hint:(1,.9)
                        pos_hint:{'center_x':.5,'center_y':.39}
                        md_bg_color:[215/255,255/255,210/255,1]
                        radius:[15]
                        ScrollView:
                            MDList:
                                ThreeLineAvatarListItem:
                                    on_release:root.manager.current='worker_profile'
                                    text:'Name1'
                                    secondary_text:'Age'
                                    tertiary_text:'Work'
                                    ImageLeftWidget:
                                        source:'blank_person.jpg'


                                ThreeLineAvatarListItem:
                                    text:'Name2'
                                    secondary_text:'Age'
                                    tertiary_text:'Work'
                                    ImageLeftWidget:
                                        source:'blank_person.jpg'
                                ThreeLineAvatarListItem:
                                    text:'Name3'
                                    secondary_text:'Age'
                                    tertiary_text:'Work'
                                    ImageLeftWidget:
                                        source:'blank_person.jpg'
                                ThreeLineAvatarListItem:
                                    text:'Name4'
                                    secondary_text:'Age'
                                    tertiary_text:'Work'
                                    ImageLeftWidget:
                                        source:'blank_person.jpg'
                                ThreeLineAvatarListItem:
                                    text:'Name5'
                                    secondary_text:'Age'
                                    tertiary_text:'Work'
                                    ImageLeftWidget:
                                        source:'blank_person.jpg'

                                ThreeLineAvatarListItem:
                                    text:'Name6'
                                    secondary_text:'Age'
                                    tertiary_text:'Work'
                                    ImageLeftWidget:
                                        source:'blank_person.jpg'
                                ThreeLineAvatarListItem:
                                    text:'Name7'
                                    secondary_text:'Age'
                                    tertiary_text:'Work'
                                    ImageLeftWidget:
                                        source:'blank_person.jpg'
                                ThreeLineAvatarListItem:
                                    text:'Name8'
                                    secondary_text:'Age'
                                    tertiary_text:'Work'
                                    ImageLeftWidget:
                                        source:'blank_person.jpg'  
        MDNavigationDrawer:
            id:nav_draw
            BoxLayout:
                orientation: 'vertical'
                spacing:'8dp'
                padding:'8dp'
                Image:
                    source:'farm.jpg'
                    size_hint_y:None
                    allow_stretch:True
                MDLabel:
                    text:"Welcome to WorkFarma"
                    font_style:'Subtitle1'
                    size_hint_y:None
                    height:self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            id:click 
                            text:'filter'
                            IconLeftWidget:
                                icon:'filter'
                        MDRaisedButton:
                            text:"LOGOUT"
                            on_press:root.manager.current="login"

<Worker_profile>
    name:'worker_profile'
    Image:
        source:'blank_person.jpg'
        pos_hint:{'center_x':0.2002,'center_y':0.8}
        size_hint:(0.3,0.5)
    MDLabel:
        text:"NAME:Worker-1"
        halign:'center'
        pos_hint:{'center_x':0.7,'center_y':0.9}
    MDLabel:
        text:"AGE:21"
        halign:'center'
        pos_hint:{'center_x':0.6,'center_y':0.8}
    MDLabel:
        text:"EXPERIENCE:2yrs"
        halign:'center'
        pos_hint:{'center_x':0.7,'center_y':0.7}
    MDLabel:
        text:"Worker-1 is a very talented person and very hardworking.Very Humble and soft natured --Sathvik"
        halign:'center'
        pos_hint:{'center_x':0.5,'center_y':0.5}
    MDLabel:
        text:"Worker-1 has rating 4.58/5"
        halign:'center'
        pos_hint:{'center_x':0.5,'center_y':0.4}
    MDLabel:
        text:"Preffered Work Timings:12PM-8PM"
        halign:'center'
        pos_hint:{'center_x':0.5,'center_y':0.3}
    MDLabel:
        text:"Locality:Zaheerabad"
        halign:'center'
        pos_hint:{'center_x':0.5,'center_y':0.2}

    MDRaisedButton:
        text:"Book-Now!"
        pos_hint:{'center_x':0.8,'center_y':0.1}
        on_press:root.manager.current="checkout"
    MDRaisedButton:
        text:"Back"
        pos_hint:{'center_x':0.15,'center_y':0.1}
        on_press:root.manager.current="worker"
<checkout>
    name:'checkout'
    MDLabel:
        text:"checkout"
        font_style:"H4"
        pos_hint:{'center_x':0.5,'center_y':0.5}
    MDRaisedButton:
        text:"Back"
        pos_hint:{'center_x':0.15,'center_y':0.1}
        on_press:root.manager.current="worker"


















"""
class MenuScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class SignupScreen(Screen):
    pass
class SignupScreen1(Screen):
    pass
class Workers_list(Screen):
    """workers"""
class Worker_profile(Screen):
    pass
class checkout(Screen):
    pass
sm=ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
class FARMA(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Green"
        self.theme_cls.theme_style="Dark"
        screen = Builder.load_string(screen_helper)

        return screen

FARMA().run()
