import requests
import random

base_url = 'https://pokeapi.co/api/v2/'

def choose_random_pokemon():
    rand_id = random.randint(0, 1025)
    url = f'{base_url}pokemon/{rand_id}'
    response = requests.get(url)
    data = response.json()
    name = data['name']
    return name

def get_pokemon_data(pokemon):
    response = requests.get(f'{base_url}pokemon/{pokemon}')
    data = response.json()
    return data

def get_moves(pokemon_data):
    return pokemon_data['moves']

def randomize_moves(moves):
    poss_moves = []
    for move in moves:
        url = move['move']['url']
        move_data = get_move_info(url)
        if move_data['damage_class']['name'] == 'physical' and (move_data.get('power', 0) or 0) != 0:
            poss_moves.append(move_data)
    chosen = random.sample(poss_moves, 3)
    poke_moves = []
    for move in chosen:
        poke_moves.append(move)
    return poke_moves

def get_move_info(url):
    response = requests.get(url)
    data = response.json()
    return data

def random_iv():
    return random.randint(0, 31)