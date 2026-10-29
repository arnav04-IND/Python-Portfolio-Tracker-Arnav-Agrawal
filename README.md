# Stock Portfolio Manager

A simple command-line portfolio tracker I built in Python. You enter the stocks you own, and it saves them in a JSON file, pulls current prices from Yahoo Finance using `yfinance`, shows your profit/loss, and plots a pie chart of how your portfolio is split.

I made this to practice working with APIs, file handling and data visualization in Python.

## What it does

- **Add holdings**: enter a ticker (like `TCS.NS`, `RELIANCE.NS` or `AAPL`), the quantity, and your buying price
- **List holdings**: shows everything saved in `Portfolio.json`
- **Summary**: fetches the latest closing price and shows the P/L for each stock and overall
- **Allocation chart**: pie chart of your portfolio based on current market value

## Requirements

- Python 3.10 or above (I used `match-case`, which isn't available in older versions)
- [yfinance](https://pypi.org/project/yfinance/)
- [matplotlib](https://pypi.org/project/matplotlib/)

## How to run

1. Clone the repo
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. (Optional) Make a virtual environment
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

3. Install the libraries
   ```bash
   pip install yfinance matplotlib
   ```

4. Run it
   ```bash
   python portfolio.py
   ```

## Using it

Once it runs, you get this menu:

```text
Portfolio Manager

1. Add holdings
2. List holdings
3. Display summary
4. Plot portfolio allocation
5. Exit

Enter your choice:
```

Just type the number of the option you want.

**About ticker symbols:** use the same symbols as Yahoo Finance. For NSE stocks add `.NS` at the end (e.g. `TCS.NS`), and for BSE stocks add `.BO`. US stocks like `AAPL` work without anything extra.

## Files

```text
├── portfolio.py     # main program
├── Portfolio.json   # where your holdings get saved
└── README.md
```

## Notes

- You need an internet connection for the summary and chart, since prices come from Yahoo Finance.
- The price used is the latest closing price, not a live tick-by-tick price.
- This is a learning project, not financial advice.
