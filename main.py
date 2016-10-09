from tkinter import *
from UserInterface import *

def main():
    root = Tk()
    root.geometry("1920x1080+300+300")
    app = Paint(root)
    root.mainloop()

if __name__ == "__main__":
    main()

