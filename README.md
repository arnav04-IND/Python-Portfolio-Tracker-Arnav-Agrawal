# Python-Portfolio-Tracker-Arnav-Agrawal
Python based investment portfolio tracker
# Stock Portfolio Manager

A command-line stock portfolio tracker built with Python. It stores your stock holdings locally in JSON format, fetches real-time market prices using Yahoo Finance (`yfinance`), calculates profit/loss across your positions, and visualizes portfolio allocation with `matplotlib`.

## Features

- **Add Holdings**: Record stock ticker symbols (e.g., `TCS.NS`, `RELIANCE.NS`, `AAPL`), quantity, and buying price.
- **List Holdings**: View all saved stock positions stored in `Portfolio.json`.
- **Live Profit/Loss Summary**: Fetch the latest closing price via Yahoo Finance to compute per-stock and overall Profit/Loss (P/L).
- **Portfolio Allocation Chart**: Generate a pie chart showing the percentage breakdown of your portfolio by current market value.

## Tech Stack & Dependencies

- **Python 3.10+** (uses `match-case` structural pattern matching)
- [yfinance](https://pypi.org/project/yfinance/) — For fetching live market data from Yahoo Finance
- [matplotlib](https://pypi.org/project/matplotlib/) — For plotting the portfolio allocation pie chart

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install yfinance matplotlib
```

### 4. Run the application

```bash
python portfolio.py
```

## Usage

When you run `portfolio.py`, an interactive menu appears:

```text
Portfolio Manager

1. Add holdings
2. List holdings
3. Display summary
4. Plot portfolio allocation
5. Exit

Enter your choice:
```

- **Note on Ticker Symbols**: Use standard Yahoo Finance ticker symbols. For Indian NSE stocks, append `.NS` (e.g., `TCS.NS`, `RELIANCE.NS`). For BSE stocks, append `.BO`.

## Project Structure

```text
├── portfolio.py     # Main CLI application and portfolio logic
├── Portfolio.json   # Local JSON storage for stock holdings
└── README.md        # Project documentation
```
