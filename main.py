import sys
import random
import json
from functions import *
from pokemon import pokemon

if len(sys.argv) == 3:
    poke_name_1 = sys.argv[1]
    poke_name_2 = sys.argv[2]
elif len(sys.argv) == 2:
    if sys.argv[1] == 'random':
        poke_name_1 = choose_random_pokemon()
        poke_name_2 = choose_random_pokemon()
    else:
        print('Usage: [pokemon <name1> <name2>] or [pokemon random]')
        sys.exit()
else:
    print('Usage: [pokemon <name1> <name2>] or [pokemon random]')
    sys.exit()

poke1 = pokemon(poke_name_1)
print(poke1)
# print(json.dumps(poke1.data, indent=4))

poke2 = pokemon(poke_name_2)
print(poke2)

move_order = first_mover(poke1, poke2)
use_move1 = move_order[0].use_rand_move(move_order[1])
print(use_move1[2])
use_move2 = move_order[1].use_rand_move(move_order[0])
print(use_move2[2])