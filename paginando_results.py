import requests

# 1 - Autenticação via Github
access_token = ''
headers = {
    'Authorization': 'Bearer ' +access_token,
    'X-GitHub-Api-Version': '2022-11-28'
    
}
# 2 - Mapeando Informações
base_api = 'https://api.github.com'
user = 'OneBitCodeBlog'
url = f'{base_api}/users/{user}/repos?page=2'


# 3 - Organizando os Dados
repos_list = []
for page_num in range(1, 3):
    try:
        url_page = f'{url}?page={page_num}'
        response = requests.get(url, headers=headers)
        repos_list.append(response.json())
    except:
        repos_list.append(None)
    

# 4 - Apresentar os dados
print(len(repos_list))
print(repos_list[0][2]['name'])