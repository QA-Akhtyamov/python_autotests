"""
Test api pokemonbattle.me
"""

import requests
URL = 'https://api.pokemonbattle.me:9104'
HEADER={'Content-Type':'application/json','trainer_token':'b900953b95cd056e8b0203ac795bbdd6'}

"""Создание покемона"""
'''response = requests.post(f'{URL}/pokemons',json = 
                        {"name":"general",
                        "photo":"https://dolnikov.ru/pokemons/albums/001.png"},
                        headers=HEADER)
print(f'Статус код:{response.status_code},Сообщение{response.json()["message"]}')'''


"""Смена имени покемона"""
"""response = requests.put(f'{URL}/pokemons',json = 
    {"pokemon_id": "28075",
    "name": "mauris",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"}, 
     headers=HEADER)
print(f'Статус код:{response.status_code},Сообщение{response.json()["message"]}')"""


"""Поймать покемона в покебол"""
"""response = requests.post(f'{URL}/trainers/add_pokeball',json = 
                         { "pokemon_id": "28075"},
                         headers=HEADER)
print(f'Статус код:{response.status_code},Сообщение{response.json()["message"]}')"""