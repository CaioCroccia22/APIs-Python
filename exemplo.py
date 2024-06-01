import requests


# 1 - Vendo a versão
print(requests.__version__)

# 2 - Vendo os métodos
# print(dir(requests))

# 3 - Realizando requisição GET
link = 'https://www.google.com/search?client=opera-gx&q=Palmeiras'

requisicao = requests.get(link)
print(requisicao)
print(requisicao.status_code)
print(requisicao.text)
