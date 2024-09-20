import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '406a5101c822af52131f7a972ec0558c'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}
TRAINER_ID='5420'

def test_status_code ():
    response=requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response.status_code==200
    
def test_part_of_response():
    response_get=requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response_get.json()["data"] [0]['trainer_name']=="Mini"