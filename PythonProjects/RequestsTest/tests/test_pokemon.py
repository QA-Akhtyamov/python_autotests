import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER={'Content-Type':'application/json','trainer_token':'b900953b95cd056e8b0203ac795bbdd6'}

def test_gef_trainers():
    response=requests.get(f'{URL}/trainers',params={'trainer_id':3912},timeout=5)
    assert response.status_code==200,'Unexpested status code'
    assert response.json()['trainer_name']=="Азамат", ''