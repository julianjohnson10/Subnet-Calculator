import Model
import View
import tkinter as Tk

class Controller():
    def __init__(self) -> None:
        self.root = Tk.Tk()
        self.model = Model()
        self.view = View(self.root)

    def run(self):
        self.root.title("Subnet Tool")
        self.root.deiconify()
        self.root.mainloop()
        