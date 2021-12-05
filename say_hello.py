from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
  def build(self):
    self._set_window()
    self._set_logo_and_question("what is your name")
    self._set_textinput()
    self._set_button()
    
    return self.window
  
  def callback(self,instance):
    self.greetting.text = f"Hello {self.user.text} !"
    
    
  def _set_window(self):
    self.window = GridLayout()
    self.window.cols = 1
    
    self.window.size_hint = (0.6, 0.7)
    self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5 }
    
  def _set_logo_and_question(self, ques):
    self.window.add_widget(Image(source="logo.png"))
    self.greetting = Label(
      text=ques,
      font_size=18,
      color="#00FFCE"
    )
    self.window.add_widget(self.greetting)
    
  def _set_textinput(self):
    self.user = TextInput(
      multiline=False,
      padding_y=(20,20),
      size_hint=(1,0.5)
    )
    self.window.add_widget(self.user)
    
    
  def _set_button(self):
    self.button = Button(
      text="Greet",
      size_hint=(1,0.5),
      bold=True,
      background_color="#00FFCE"
    )
    
    self.button.bind(on_press=self.callback)
    self.window.add_widget(self.button)
  
  
if __name__ == "__main__":
  SayHello().run()