from tkinter import *
class View(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #add a label
        self.label = Label(self, text="test")
        self.label.grid(row=1, column=0)
        
        self.ip_addr = StringVar()

        #add a button
        self.button = Button(self, text="OK")

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller
    
    def save_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.save(self.ip_addr.get())