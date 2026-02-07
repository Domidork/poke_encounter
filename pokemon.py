from functions import *
import random

class pokemon():
    def __init__(self, name):
        self.data = get_pokemon_data(name)
        self.name = name
        self.possible_moves = get_moves(self.data)
        self.moves = randomize_moves(self.possible_moves)
        self.health = self.data['stats'][0]['base_stat']

    def __str__(self):
        lines = []

        lines.append(f'\n------{self.data['name'].capitalize()}------')
        lines.append(f'Health: {self.data['stats'][0]['base_stat']}')
        lines.append('Moves:')
        
        for move in self.moves:
            lines.append(f'\t{move['name']}: {move.get('power', 0) or 0}')

        lines.append("")

        return '\n'.join(lines)
    
    def take_damage(self, other, inflicted):
        self.health -= inflicted
        return f'{other.name} dealt {inflicted}dmg to {self.name}!\n{self.name} is now at {self.health}hp!'

    def use_rand_move(self, other):
        choice = random.choice(self.moves)
        move_name = choice['name']
        move_dmg = choice.get('power', 0) or 0
        # Inflicts the damage on the target pokemon
        dmg_message = other.take_damage(self, move_dmg)
        # --------------
        return (move_name, move_dmg, dmg_message)