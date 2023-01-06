#This code prompts a desktop notification with stock information about the ticker
#that the user has input.

# Import the necessary modules
import tkinter as tk
from tkinter import simpledialog
import requests
import sys

# Import the notification library
from plyer import notification

# Define a function that will get the stock data and show a desktop notification
def get_stock_data(ticker):

    # Use the API key and the stock ticker to get the stock data
    API_KEY = "cf11d6a9d5d03f2ade358f74a882c5c0"
    API_URL = "https://financialmodelingprep.com/api/v3/quote/"
    stock_data = requests.get(API_URL + ticker, params={"apikey": API_KEY}).json()

    # Check if the stock data entered in the ticker by the user is valid
    if not stock_data:
        
        # Show an error message in the desktop notification
        notification.notify(
            title="Error",
            message=ticker.upper()+ " " + "is not a valid ticker. \
            \nPlease try again."
        )
    else:
        
        # Extract the data we need from the stock data
        name = stock_data[0]["name"]
        price = stock_data[0]["price"]
        high = stock_data[0]["dayHigh"]
        low = stock_data[0]["dayLow"]
        prev_close = stock_data[0]["previousClose"]

        # Show a desktop notification with the stock data
        notification.notify(
            title="Stock Data: " + name.upper(),
        message=f"Price: ${price:,.2f} \
        \nToday's High: ${high:,.2f} \
        \nToday's Low: ${low:,.2f} \
        \nPrevious Close: ${prev_close:,.2f}"
        )

# Create a window and ask the user to enter a stock ticker
root = tk.Tk()
root.withdraw()
ticker = simpledialog.askstring("Stock Desktop Notifier ", "Enter a stock ticker:")

# Call the function to get the stock data and show a notification
get_stock_data(ticker)
