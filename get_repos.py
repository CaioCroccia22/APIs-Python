import requests

# 1 - Mapeando a informação 

headers = {'X-GitHub-Api-Version': '2022-11-28'}


base_api = 'https://api.github.com'
user = 'OneBitCodeBlog'
url = f'{base_api}/users/{user}/repos'

# print(url)


# 2 - Realizando a requisição
response = requests.get(url, headers=headers)
print(response.status_code)
# print(len(response.json()))
# print(response.json())