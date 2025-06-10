from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
from anvil import media

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("klasifikasi",self.file_loader_1.file)
    text=anvil.server.call("hasil")
    self.label_4.text=text
    pass
