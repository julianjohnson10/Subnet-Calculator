import Controller
from tkinter import *

def main():
    root = Tk()
    frame = Frame(root)
    root.title = "Subnet Tool"
    app = Controller(root)
    root.mainloop()

if __name__ == '__main__':
    main()