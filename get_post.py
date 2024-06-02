import requests

#  API JsonPlaceHolder
url = 'https://jsonplaceholder.typicode.com/posts/1'

# 2 - Enviando requisição get
response = requests.get(url)
print(response)
print(response.status_code)


# 3 - Tratamento de dados

if response.status_code == 200:
    print('Código retornado com sucesso')
else:
    print('A requisição não foi processada corretamente')
    
    
# 4 - Pegar os dados
# Essa função pega os dados de resposta e converte para JSON
response_json = response.json()
print(response_json)

# Json como xml são arquivos fáceis de ser lidos
# Pega as informações da API em formato JSON e passa para outra aplicação 