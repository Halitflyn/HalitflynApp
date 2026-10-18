from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class HalitflynApp(App):
    def build(self):
        layout = BoxLayout()
        label = Label(
            text='Halitflyn',
            font_size='48sp',
            bold=True,
            halign='center',
            valign='middle'
        )
        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    HalitflynApp().run()

