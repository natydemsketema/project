from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
class main_App(MDApp):
    def build(self):
        return MDLabel(text="welcoe to my app",halign="center")
if __name__=='__main__':
    main_App().run()
        
