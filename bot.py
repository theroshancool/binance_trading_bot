import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException
import time


# Set up logging
logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        logging.info("Initialized Binance Futures Client on Testnet")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                "symbol": symbol,
                "side": side.upper(),
                "type": order_type.upper(),
                "quantity": quantity,
            }

            if order_type.upper() == 'LIMIT':
                params.update({
                    "timeInForce": "GTC",
                    "price": price
                })

            response = self.client.futures_create_order(**params)
            logging.info(f"Order placed: {response}")
            return response

        except BinanceAPIException as e:
            logging.error(f"Binance API Error: {e}")
            return {"error": str(e)}
        except Exception as e:
            logging.error(f"Unexpected Error: {e}")
            return {"error": str(e)}

def main():
    import getpass

    api_key = input("o9pQ5eTafZYUmqcDcq3PKJTyXyldg0f0vxnqLSrq4hjpKYyFUFPe61ArJ8slRtwC")
    api_secret = getpass.getpass("8oaIJQ32cQWObIanHEKKLpiVYXqUnL7ZVd7Z7GIpAb8xiouTcNc75BUH2KvBgJct")

    bot = BasicBot(api_key, api_secret)

    while True:
        print("\nOptions: [1] Buy [2] Sell [3] Exit")
        choice = input("Choose an action: ")

        if choice == "3":
            break

        symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
        side = 'BUY' if choice == "1" else 'SELL'
        order_type = input("Enter order type (MARKET / LIMIT): ").upper()
        quantity = float(input("Enter quantity: "))
        price = None
        if order_type == 'LIMIT':
            price = float(input("Enter price: "))

        result = bot.place_order(symbol, side, order_type, quantity, price)
        print(result)

if __name__ == "__main__":
    main()