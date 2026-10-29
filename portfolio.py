import json
import os
import yfinance as yf
import matplotlib.pyplot as plt

DATA_FILE= "Portfolio.json"

def load_holdings():
    if not os.path.exists(DATA_FILE):
        return[]
    file= open (DATA_FILE, "r")
    holdings= json.load(file)
    file.close()
    return holdings

def save_holdings(holdings):
    file= open(DATA_FILE, "w")
    json.dump(holdings, file, indent=2)
    file.close()

def add_holdings(code, qty, buy_price):
    holdings= load_holdings()
    new_stock= {"code": code.upper(), "qty": qty, "buy_price": buy_price}
    holdings.append(new_stock)
    save_holdings(holdings)
    print("Added.", code.upper())

def list_holdings():
    holdings= load_holdings()
    if len(holdings) ==0:
        print("Holdings are empty.")
        return
    for stock in holdings:
        print(stock["code"], stock["qty"], stock["buy_price"])

def display_summary():
    holdings= load_holdings()
    if len(holdings) == 0:
        print("Holdings are empty.")
        return

    total_profit_loss= 0

    for stock in holdings:
        code= stock["code"]
        qty= stock["qty"]
        buy_price= stock["buy_price"]

        ticker= yf.Ticker(code)
        data= ticker.history(period="1d")
        if data.empty:
            print(code, "| Could not fetch price.")
            continue

        current_price= float(data["Close"].iloc[-1])

        profit_loss= (current_price - buy_price) * qty
        total_profit_loss += profit_loss

        print(code, "| Buy:", buy_price, "| Latest:", round(current_price, 2), "| P/L:", round(profit_loss, 2))

    if total_profit_loss >= 0:
        print("Overall Profit:", round(total_profit_loss, 2))
    else:
        print("Overall Loss:", round(total_profit_loss, 2))

def plot_allocation():
    holdings= load_holdings()
    if len(holdings) == 0:
        print("Holdings are empty.")
        return

    labels= []
    values= []

    for stock in holdings:
        code= stock["code"]
        qty= stock["qty"]

        ticker= yf.Ticker(code)
        data= ticker.history(period="1d")
        if data.empty:
            print(code, "| Could not fetch price, skipping in chart.")
            continue

        current_price= float(data["Close"].iloc[-1])
        current_value= current_price * qty

        labels.append(code)
        values.append(current_value)

    if len(values) == 0:
        print("No valid stock prices found to plot.")
        return

    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Portfolio Allocation by Current Value")
    plt.show()


# add_holdings("tcs.ns", 5, 3900)
# add_holdings("reliance.ns", 10, 2450.5)
# list_holdings()

print("Portfolio Manager")

def menu(status_code):
   match status_code:
       case 1: 
           code= input("Enter the name of the stock: ")
           qty= int(input("Enter the quantity of the the stock: "))
           buy_price= float(input("Enter the buying price of the stock: "))
           add_holdings(code, qty, buy_price)
           return True

       case 2: 
           list_holdings()
           return True

       case 3:
           display_summary()
           return True

       case 4:
           plot_allocation()
           return True

       case 5:
           return False

       case _:
           print("Invalid choice. Please try again.")
           return True

flag= True
while flag:
    print()
    print("1. Add holdings")
    print("2. List holdings")
    print("3. Display summary")
    print("4. Plot portfolio allocation")
    print("5. Exit")
    print()
    status_code= int(input("Enter  your choice: "))
    flag= menu(status_code)
