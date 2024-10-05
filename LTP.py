from googlefinance import getQuotes
import json
def getdata(security):
	while True:
		try:
			price = json.dumps(getQuotes(security))
			data = json.loads(price)
			price = data[0]['LastTradePrice']
			return float(price)
		except:
			continue
data = getdata("NASDAQ:AAPL")
print(data)
