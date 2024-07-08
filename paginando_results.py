import requests

# 1 - Autenticação via Github
access_token = ''
headers = {
    'Authorization': 'Bearer ' +access_token,
    'X-GitHub-Api-Version': '2022-11-28'
}