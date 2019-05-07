
import requests
import json

requisicao = requests.get('https://api.bitcointrade.com.br/v1/public/BTC/ticker')
print('*********BITCOIN TRADE*********')
print('-----------------------------------------------------')

cotacao = json.loads(requisicao.text)
print('BTC/USD: ', cotacao['data']['last'])
print('Buy: ', cotacao['data']['buy'], '<------> Sell: ',cotacao['data']['sell'] )

requisicao = requests.get('https://api.bitcointrade.com.br/v1/public/ETH/ticker')
print('-----------------------------------------------------')
cotacao = json.loads(requisicao.text)
print('ETH/BRL: ', cotacao['data']['last'])
print('Buy: ', cotacao['data']['buy'], '<------> Sell: ',cotacao['data']['sell'] )

requisicao = requests.get('https://api.bitcointrade.com.br/v1/public/LTC/ticker')
print('-----------------------------------------------------')
cotacao = json.loads(requisicao.text)
print('LTC/BRL: ', cotacao['data']['last'])
print('Buy: ', cotacao['data']['buy'], '<------> Sell: ',cotacao['data']['sell'] )

requisicao = requests.get('https://api.bitcointrade.com.br/v1/public/BCH/ticker')
print('-----------------------------------------------------')
cotacao = json.loads(requisicao.text)
print('BCH/BRL: ', cotacao['data']['last'])
print('Buy: ', cotacao['data']['buy'], '<------> Sell: ',cotacao['data']['sell'] )
