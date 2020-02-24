import yfinance as yf
import pandas as pd
import tkinter as tk
import pygubu
import matplotlib.pyplot as plt
import numpy as np
import datetime
import csv

data = []
with open('app/tickers.csv') as f:
    for row in csv.reader(f):
        data.append(row[0])

print(data)
ticker = yf.download(data, period='max')
start_date = input("Input starting year with format mm/dd/yy:")

date = datetime.datetime.strptime(start_date, "%m/%d/%y")

print("Starting date is: ", date)

while True:
    print(date)
    try:
        print(ticker['Open'].loc[date])
    except:
        print("Markets down today")
    choice = input("advance, purchase, stop")
    if choice == 'stop':
        break
    if choice == 'advance':
        day = int(input("How many days? "))
        date = date + datetime.timedelta(days=day)


# year = input("Please enter starting year: ")

# ticker = yf.download(['TSLA', 'MSFT'], period='ytd')
# ticker['Close'][input('Which stock do you want to see?')].plot(title="stock price")
# plt.show()


# class Application:
#     def __init__(self, master):
#         self.builder = builder = pygubu.Builder()
#         builder.add_from_file('gui.ui')
#         self.application = builder.get_object('Frame_1', master)

# if __name__ == '__main__':
#     root = tk.Tk()
#     app = Application(root)
#     root.mainloop()

# try:
#     year = int(year)
# except ValueError:
#     print("retry")
