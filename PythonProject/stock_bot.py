import yfinance as yf
import json
import time

def get_stock_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        price = stock.info["currentPrice"]
        return price
    except:
        print(f"Error getting price for {symbol}")
        return None
def initialize_stocks():
    stocks = {
        "AAPL": {"current_price": None, "previous_price": None, "history": []},
        "NVDA": {"current_price": None, "previous_price": None, "history": []},
        "AMZN": {"current_price": None, "previous_price": None, "history": []}
    }
    return stocks


def update_prices(stocks_data):
    symbols = ["AAPL", "NVDA", "AMZN"]

    for symbol in symbols:
        new_price = get_stock_price(symbol)

        if new_price is not None:
            stocks_data[symbol]["previous_price"] = stocks_data[symbol]["current_price"]
            stocks_data[symbol]["current_price"] = new_price
            stocks_data[symbol]["history"].append(new_price)


def show_alert(stocks_data):
    print("\n" + "=" * 50)
    print("Stock Price Update")
    print("=" * 50)

    for symbol, data in stocks_data.items():
        current = data["current_price"]
        previous = data["previous_price"]

        if previous is None:
            print(f"{symbol}: ${current} (First check)")
            continue

        change = current - previous

        if change > 0:
            emoji = "📈"
            direction = f"UP ${change:.2f}"
        elif change < 0:
            emoji = "📉"
            direction = f"DOWN ${abs(change):.2f}"
        else:
            emoji = "➡️"
            direction = "NO CHANGE"

        print(f"{emoji} {symbol}: ${current} ({direction})")
def save_stocks(stocks_data):
    with open("stocks.json", "w") as file:
        json.dump(stocks_data, file, indent=2)
def load_stocks():
    try:
        with open("stocks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return initialize_stocks()


def run_bot():
    stocks_data = load_stocks()

    print("Starting Stock Price Tracker Bot...")
    print("Checking prices every 5 minutes. Press Ctrl+C to stop.")

    while True:
        update_prices(stocks_data)
        show_alert(stocks_data)
        save_stocks(stocks_data)

        print("Waiting 5 minutes until next check...")
        time.sleep(300)
if __name__ == "__main__":
    run_bot()