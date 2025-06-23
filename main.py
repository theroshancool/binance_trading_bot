from binance.client import Client
import time

API_KEY = 'o9pQ5eTafZYUmqcDcq3PKJTyXyldg0f0vxnqLSrq4hjpKYyFUFPe61ArJ8slRtwC'
API_SECRET = '8oaIJQ32cQWObIanHEKKLpiVYXqUnL7ZVd7Z7GIpAb8xiouTcNc75BUH2KvBgJct'

client = Client(API_KEY, API_SECRET,testnet=True)

client.get_account()

print(client.get_symbol_ticker(symbol='BTCUSD'))