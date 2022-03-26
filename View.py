import Controller
import tkinter as Tk

class View(Tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #add a label
        self.label = Tk.Label(self, text="test")
        
        #add a button
        self.button = Tk.Button(self, text="OK")

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller