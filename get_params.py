import requests


# 1 - API JsonPlaceHolde
url = 'https://jsonplaceholder.typicode.com/posts/'

# 2 - Adicionando o payload
payload = {
    "id": [1, 2, 3, 4, 5],
    "userId": 1
}

# 3 - Realizando requisição
response = requests.get(url, params=payload)
# print(response)
# print(response.json())

# 4 - Melhorar a legibilidade
response_json = response.json()
for i in response_json:
    print(i, '/n')