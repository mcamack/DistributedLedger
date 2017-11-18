import sys, pprint, requests

coin = sys.argv[1]
# pp = pprint.PrettyPrinter(indent=4)

def getRate(coin):
    return requests.get('https://api.coinmarketcap.com/v1/ticker/%s/?convert=USD' %coin).json()

print(getRate('bitcoin')[0]['price_usd'])