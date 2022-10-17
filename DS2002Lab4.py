import json
import requests
import pandas
from datetime import date

stock = input("What stock would you like information about?")

urlQuote = 'https://query1.finance.yahoo.com/v7/finance/quote'
queryString = {"symbols": stock}

url2 = 'https://query1.finance.yahoo.com/v10/finance/quoteSummary/' + stock + '?modules=financialData'
queryString2 = {'symbol': stock, 'modules': 'financialData'}

header_var = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}
response = requests.request("GET", urlQuote, headers=header_var, params=queryString)
response2 = requests.request("GET", url2, headers=header_var, params=queryString2)

stock_json = response.json()
stock_json2 = response2.json()

test = False
while not test:
    try:
        tickerName = stock_json['quoteResponse']['result'][0]['symbol']
        fullName = stock_json['quoteResponse']['result'][0]['longName']
        currentPrice = str(stock_json['quoteResponse']['result'][0]['regularMarketPrice'])
        targetMeanPrice = str(stock_json2['quoteSummary']['result'][0]['financialData']['targetMeanPrice']['fmt'])
        cashOnHand = str(stock_json2['quoteSummary']['result'][0]['financialData']['totalCash']['longFmt'])
        profitMargins = str(stock_json2['quoteSummary']['result'][0]['financialData']['profitMargins']['fmt'])
        print("Ticker Name: " + tickerName)
        print("Full Name: " + fullName)
        print("Current Price: " + currentPrice)
        print("Target Mean Price: " + targetMeanPrice)
        print("Cash on Hand: " + cashOnHand)
        print("Profit Margins: " + profitMargins)

        company = {
            "datePulled": date.today().strftime("%B %d, %Y"),
            "tickerName": tickerName,
            "fullName": fullName,
            "currentPrice": currentPrice,
            "targetMeanPrice": targetMeanPrice,
            "cashOnHand": cashOnHand,
            "profitMargins": profitMargins
        }

        json_object = json.dumps(company)
        with open("company.json", "w") as outfile:
            outfile.write(json_object)

        test = True
    except:
        print("Sorry, that is not a valid stock ticker name.")
        test = True