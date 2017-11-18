import sys, pprint, requests

def getRate(coin):
    return requests.get('https://api.coinmarketcap.com/v1/ticker/%s/?convert=USD' %coin).json()

print(getRate('bitcoin')[0]['price_usd'])
print(getRate('zcash')[0]['price_usd'])