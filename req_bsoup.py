import pandas as pd
import requests
from bs4 import BeautifulSoup
# 1 - Coletando vagas em python
response = requests.get('https://hipnoise.com.br/roupas/c')
print(response.status_code)

# print(response.text)

soup = BeautifulSoup(response.text, 'lxml')
clothes = soup.find_all('div', class_='product-info-wrapper')
print(len(clothes))


brands = []
prices = []
# 2 - Estruturando informação para coleta
for clothe in clothes:
    brand_name = clothe.find('h3', class_='h3').text.strip()
    print(brand_name)
    price_element = clothe.find('span', class_='price')
    if price_element:
        price_clothe = price_element.get_text(strip=True)
        print(price_clothe)
    else:
        print("Price not found")       
# 3 - Exportando para arquivo CSV
    brands.append(brand_name)
    prices.append(price_element)
python_clothes = pd.DataFrame()
python_clothes['Brands'] = brands
python_clothes['prices'] = prices 
print(python_clothes)
python_clothes.to_csv('Lista_de_roupas.csv')