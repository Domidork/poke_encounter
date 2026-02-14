import requests
import random
import json
import os

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
    dir = os.path.dirname(os.path.realpath(__file__))
    with open(f'{dir}/move_data.json', 'r', encoding='utf-8') as file:
        moves = json.load(file)

    moves_for_poke = []
    poke_moves = []
    poke_moves_data = []
    for move_entry in pokemon_data['moves']:
        name = move_entry['move']['name']
        poke_moves.append(name)
    for move_entry in moves:
        if move_entry['identifier'] in poke_moves:
            poke_moves_data.append(move_entry)
    return poke_moves_data

def randomize_moves(moves):
    poss_moves = []
    for move in moves:
        if (move.get('power', 0) or 0) != 0:
            poss_moves.append(move)
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

def first_mover(poke1, poke2):
    if poke1.speed > poke2.speed:
        return poke1, poke2
    elif poke2.speed > poke1.speed:
        return poke2, poke1
    elif poke1.speed == poke2.speed:
        first = random.choice([poke1, poke2])
        if poke1 != first:
            second = poke1
        elif poke2 != first:
            second = poke2
    return first, second

def help():
    return 'Usage: [~/poke <pokemon1> <pokemon2>] or [~/poke random]\nTags: -rt (enables realtime mode)\nSpecial: --link (adds a symlink to the home directory)'