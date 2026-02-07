import requests
import random

base_url = 'https://pokeapi.co/api/v2/'

def get_pokemon_data(pokemon):
    response = requests.get(f'{base_url}pokemon/{pokemon}')
    data = response.json()
    return data

def get_moves(pokemon_data):
    return pokemon_data['moves']

def randomize_moves(moves):
    chosen = random.sample(moves, 3)
    poke_moves = []
    for move in chosen:
        url = move['move']['url']
        move_data = get_move_info(url)
        poke_moves.append(move_data)
    return poke_moves

def get_move_info(url):
    response = requests.get(url)
    data = response.json()
    return data