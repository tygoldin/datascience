import yfinance as yf
import pandas as pd
import tkinter as tk
import pygubu
import matplotlib.pyplot as plt
import numpy as np
import datetime
import csv

# loading in the tickers to be used for the stocks
data = []
with open('app/tickers.csv') as f:
    for row in csv.reader(f):
        data.append(row[0])

print(data)
start_date = input("Input starting year with format mm/dd/yy:")
# start_date = "12/13/18"
date = datetime.datetime.strptime(start_date, "%m/%d/%y")
print("Starting date is: ", date)
ticker = yf.download(data, start=date - datetime.timedelta(days=365), end=date + datetime.timedelta(days=365))



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
#         builder.add_from_file('app/gui.ui')
#         self.application = builder.get_object('Frame_1', master)
#
# if __name__ == '__main__':
#     root = tk.Tk()
#     app = Application(root)
#     root.mainloop()

# try:
#     year = int(year)
# except ValueError:
#     print("retry")
