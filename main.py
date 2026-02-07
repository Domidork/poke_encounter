import sys
import requests
import json
import random
from functions import *
from pokemon import pokemon


bulbasaur = pokemon('bulbasaur')
bulbasaur.print_stats()



# poke_data = get_pokemon_data('bulbasaur')
# moves = get_moves(poke_data)
# pokemon_moves = randomize_moves(moves)

# print(f'Health: {poke_data['stats'][0]['base_stat']}')
# for move in pokemon_moves:
#     print(f'{move['name']}: {move.get('power', 0)}')
