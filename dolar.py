from bs4 import BeautifulSoup
import requests


url = 'http://www.dolarhoy.com/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

col6 = soup.find_all('div', class_='col-6')
precio_compra = col6[0].find_all('span')
precio_venta = col6[1].find_all('span')


def decimeDolarCompra():
    return precio_compra[0].text.strip()


def decimeDolarVenta():
    return precio_venta[0].text.strip()


"""
print('Dolar Oficial Hoy')
print('Precio Compra: ' + precio_compra[0].text.strip())
print('Precio Venta: ' + precio_venta[0].text.strip())
"""
