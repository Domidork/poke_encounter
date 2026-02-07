import sys
import requests
import json
import random
from functions import *
from pokemon import pokemon


poke1 = pokemon('bulbasaur')
print(poke1)

poke2 = pokemon('charmander')
print(poke2)


use_move1 = poke1.use_rand_move(poke2)
print(use_move1[2])
use_move2 = poke2.use_rand_move(poke1)
print(use_move2[2])