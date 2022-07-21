from email import header
import json
from locale import currency
from urllib import response
from requests import Request, Session
import pprint

crypto = input("Enter A Cryptocurrency:")
currency = input("Please Enter The Converting Currency:")

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

parameters = {
    'slug':crypto,
    'convert':currency
}
 
headers = {
    'Accepts':'application/json',
    'X-CMC_PRO_API_KEY':'1f87ab63-5701-42d2-8475-864aef3d94bd'
}


session = Session()
session.headers.update(headers)
response = session.get(url, params=parameters)

if response.status_code != 200:
    print("Please Enter A Valid CryptoCurrency.")

if response.status_code == 200:
    pprint.pprint(json.loads(response.text))
