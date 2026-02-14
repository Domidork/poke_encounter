#!/usr/bin/env python3

import sys
import os
import subprocess
from functions import *
from sefuncs import rtsleep
from pokemon import pokemon

# Where the actual arguments start after tags
argstart = 1
if '--help' in sys.argv:
    print(help())
    sys.exit()
if '--link' in sys.argv:
    if not os.path.islink(str((subprocess.run(['pwd'], capture_output=True).stdout)) + '/wrapper.sh'):
        subprocess.run(['./linker.sh'], )
    else:
        print('You have already linked this program to home!')
    sys.exit()
if '-rt' in sys.argv:
    realtime = True
    argstart += 1
else:
    realtime = False
if len(sys.argv) == argstart + 2:
    poke_name_1 = sys.argv[argstart]
    poke_name_2 = sys.argv[argstart + 1]
elif len(sys.argv) == argstart + 1:
    if sys.argv[argstart] == 'random':
        poke_name_1 = choose_random_pokemon()
        poke_name_2 = choose_random_pokemon()
    else:
        print('Usage: [~/poke <pokemon1> <pokemon2>] or [~/poke random]')
        sys.exit()
else:
    print('Usage: [~/poke <pokemon1> <pokemon2>] or [~/poke random]')
    sys.exit()

poke1 = pokemon(poke_name_1)
print(poke1)
# print(json.dumps(poke1.data, indent=4))

poke2 = pokemon(poke_name_2)
print(poke2)

turn = 1
while poke1.health > 0 and poke2.health > 0:
    print(f'--------Turn {turn}--------')
    rtsleep(realtime)
    move_order = first_mover(poke1, poke2)
    use_move1 = move_order[0].use_rand_move(move_order[1])
    dmg_return1 = use_move1[2]
    print(dmg_return1[0])
    if dmg_return1[1] == False:
        break
    use_move2 = move_order[1].use_rand_move(move_order[0])
    dmg_return2 = use_move2[2]
    rtsleep(realtime)
    print(dmg_return2[0])
    if dmg_return2[1] == False:
        break
    turn += 1