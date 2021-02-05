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
with open('tickers.csv') as f:
    for row in csv.reader(f):
        data.append(row[0])

print(data)
start_date = input("Input starting year with format mm/dd/yy:")
# start_date = "12/13/18"
date = datetime.datetime.strptime(start_date, "%m/%d/%y")
print("Starting date is: ", date)
starting_funds = float(input("Input starting funds (assumed $USD):"))
ticker = yf.download(data, start=date - datetime.timedelta(days=365), end=date + datetime.timedelta(days=10000))

portfolio = {}

while True:
    print(date)
    print("Portfolio: ",portfolio)

    try:
        portfolio_value = 0
        for i in portfolio:
            portfolio_value += portfolio[i] * ticker['Open'].loc[date][i]
        print("Portfolio value: $", portfolio_value)
        print("Stock prices today:\n",ticker['Open'].loc[date])
        print("Buying power: $",starting_funds)
        print("")
    except:
        print("Markets down today")
    choice = input("advance, purchase, sell, stop:")
    if choice == 'stop':
        break
    if choice == 'purchase':
        stock = input("Which stock would you like to purchase (Input ticker)?")
        stock_price = ticker['Open'].loc[date][stock]
        print(stock + " is trading at $",stock_price,".")
        share_number = float(input("How many shares would you like to purchase?"))
        if (starting_funds - share_number*stock_price <= 0):
            print("You do not have enough buying power.")
        else:
            starting_funds = starting_funds - share_number*stock_price
            print("Purchased ", share_number, " shares for $", share_number*stock_price)
            if stock in portfolio:
                portfolio[stock] += share_number
            else:
                portfolio[stock] = share_number
    if choice == 'sell':
        stock = input("Which stock would you like to sell (Input ticker)?")
        stock_price = ticker['Open'].loc[date][stock]
        print(stock + " is trading at $",stock_price,".")
        if (stock in portfolio):
            print("You own ", portfolio[stock], " shares of ", stock, ".0")
            share_number = float(input("How many shares would you like to sell?"))
            if (portfolio[stock] - share_number < 0):
                print("You do not own enough shares of this stock to sell ", share_number, " shares.")
            else:
                portfolio[stock] -= share_number
                starting_funds += share_number*stock_price
        else:
            print("You do not own any shares of this stock.")
    if choice == 'advance':
        day = int(input("How many days? "))
        date = date + datetime.timedelta(days=day)