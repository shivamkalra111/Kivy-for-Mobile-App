from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon

class TestApp(MDApp):
    def build(self):
        
        label1 = MDLabel(text = 'Hello World', halign = 'center', theme_text_color = 'Error',
                        font_style = 'Caption')
        
        label2 = MDLabel(text = 'Hello World', halign = 'center', theme_text_color = 'Custom',
                        text_color = (1/255.0, 94/255.0, 44/255.0, 1),
                        font_style = 'Caption')
    
        return label1
    
TestApp().run()
