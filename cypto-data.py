# Python:       Program for Mining the Crypto Market Data
# Author:       Sohail Shaikh
# Created:      19-Feb-2018
# Modified:     19-Feb-2018
# Script:       crypto-data.py
# Functionalaties:  input, sleep, For & while Loop, def <Function>

import urllib.request
import json
import time

currItems = str(input("How much currencies rate you want to disply ? "))
print()


def getBitCoinPrice():
    for i in j:
        print(i['symbol'], i['price_usd'])

url = 'https://api.coinmarketcap.com/v1/ticker/?limit='+currItems
requrl = urllib.request.urlopen(url)
varhtml = requrl.read()
s = varhtml.decode("utf-8")
j = json.loads(s)     # list of dictionaries

# using function bitCoinPrice
getBitCoinPrice()
print()
print("Wait for 3 seconds....")
time.sleep(3)
print()
getBitCoinPrice()
print()
print("Thanks for using program...")

