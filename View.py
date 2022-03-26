import tkinter as tk
class View(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #add a label
        self.label = tk.Label(self, text="test")
        
        #add a button
        self.button = tk.Button(self, text="OK")

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller
        