import requests


# 1 - Dados de dicionario
new_data = {
    'userId': 1,
    'id': 1,
    'title': 'Aprendendo Python',
    'body': 'Manipulando Informações da API com requests'
}

# 2 - Endpoint da API

url = 'https://jsonplaceholder.typicode.com/posts'

# 3 - Envio de dados

post_response = requests.post(
    url,
    json=new_data
)
# Objeto javascript semelhante ao dicionario em python 

print(post_response.status_code)