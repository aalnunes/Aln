import requests
import json
cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacao = cotacao.json()
def titulo():
    print('-=-'*15, 'Conversor de Moedas', '-=-'*15)
def menu():
    print('[1] = Listar Cotações [2] Converter Moedas')
def moeda_codigo():
    print('[1] = USDBRL  [2] = EURBRL [3] = BTCBRL [4] = Sair')
def dolar():
    print(cotacao['USDBRL']['bid'])
def euro():
    print(cotacao['EURBRL']['bid'])
def bitcoin():
    print(cotacao['BTCBRL']['bid'])
def moedas_cotacoes():
    print('$ {}'.format(cotacao['USDBRL']['bid']))
    print('€ {}'.format(cotacao['EURBRL']['bid']))
    print('₿ {}'.format(cotacao['BTCBRL']['bid']))
def moeda_conversao(valor_real,codigo_moeda):
    if codigo_moeda == 'USDBRL':
        resultado = valor_real * float(cotacao['BTCBRL']['bid'])

################################################################################################################################

titulo()
menu()
user = int(input('Insira a opção acima: '))
if user == 1:
    moedas_cotacoes()
elif user == 2:
    moeda_codigo()
    user_moeda_codigo =int(input('Conforme menu acima informe o codigo da moeda para conversão: '))
    if user_moeda_codigo ==4:
        print('Obrigado volte sempre')
    else:
        while user_moeda_codigo != 4:
            valor = float(input('Informe o valor em reais para conversão: '))
            if user_moeda_codigo == 1:
                dolar_convertido = (cotacao['USDBRL']['bid'])
                dolar_convertido = float(dolar_convertido)
                resultado = valor / dolar_convertido
                print('{:.2f}'.format(resultado))
                break
            elif user_moeda_codigo == 2:
                euro_convertido = (cotacao['EURBRL']['bid'])
                euro_convertido = float(euro_convertido)
                resultado = valor / euro_convertido
                print('{:.2f}'.format(resultado))
                break
            elif user_moeda_codigo == 3:
                bitcoin_convertido = ((cotacao['BTCBRL']['bid']))
                bitcoin_convertido = float(bitcoin_convertido)
                resultado = valor / bitcoin_convertido
                print('{:.5f}'.format(resultado))
                break
            elif user_moeda_codigo == 4 :
                print('Obrigado por utilizar nosso conversor de moedas!')
                break
            else:
                print('Codigo da moeda invalido.')

                break








