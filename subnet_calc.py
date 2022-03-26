import Model, View, Controller
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Subnet Calculator Tool')

        model = Model()

        view = View(self)
        
        controller = Controller(model, view)
        
        view.set_controller(controller)

