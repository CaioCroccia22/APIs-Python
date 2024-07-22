from bs4 import BeautifulSoup
import requests

# 1 - Coletando vagas em python
response = requests.get('https://hipnoise.com.br/roupas/c')
print(response.status_code)

# print(response.text)

soup = BeautifulSoup(response.text, 'lxml')
clothes = soup.find_all('div', class_='product-info-wrapper')
print(len(clothes))

# 2 - Estruturando informação para coleta
for clothe in clothes:
    brand_name = clothe.find('h3', class_='h3').text.strip()
    print(brand_name)