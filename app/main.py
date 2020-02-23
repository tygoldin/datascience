import yfinance as yf
import tkinter as tk
import pygubu


# year = input("Please enter starting year: ")

class Application:
    def __init__(self, master):
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('gui.ui')
        self.mainframe = builder.get_object('Frame_1', master)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()

# try:
#     year = int(year)
# except ValueError:
#     print("retry")
