import requests

r = requests.get('https://viacep.com.br/ws/01001000/json/')
print(r.content)