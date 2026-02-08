from functions import *
import random

class pokemon():
    def __init__(self, name):
        self.data = get_pokemon_data(name)
        self.name = name
        self.level = 5
        self.iv = random_iv()
        self.possible_moves = get_moves(self.data)
        self.moves = randomize_moves(self.possible_moves)
        # Base stats
        self.base_health = self.data['stats'][0]['base_stat']
        self.base_attack = self.data['stats'][1]['base_stat']
        self.base_defence = self.data['stats'][2]['base_stat']
        self.base_speed = self.data['stats'][5]['base_stat']
        #--------------
        # Stat calculations
        self.health = int((((2 * self.base_health + self.iv) * self.level) / 100)) + self.level + 10
        self.attack = int(((2 * self.base_attack + self.iv) * self.level) / 100) + 5
        self.defence = int(((2 * self.base_defence + self.iv) * self.level) / 100) + 5
        self.speed = int(((2 * self.base_speed + self.iv) * self.level) / 100) + 5
        #--------------


    def __str__(self):
        lines = []

        lines.append(f'\n------{self.data['name'].capitalize()}------')
        lines.append(f'Health: {self.data['stats'][0]['base_stat']}')
        lines.append('Moves:')
        
        for move in self.moves:
            lines.append(f'\t{move['identifier']}: {move.get('power', 0) or 0}')

        lines.append("")

        return '\n'.join(lines)
    

    #takes damage as well as printing message about the damage and health
    def take_damage(self, other, inflicted):
        dmg = int(((((2*other.level)/5)+2)*other.attack * (inflicted/self.defence))/50 + 2)
        self.health -= dmg
        return f'{other.name} dealt {dmg}dmg to {self.name}!\n{self.name} is now at {self.health}hp!'

    def use_rand_move(self, other):
        choice = random.choice(self.moves)
        move_name = choice['identifier']
        move_dmg = choice.get('power', 0) or 0
        # Inflicts the damage on the target pokemon
        dmg_message = other.take_damage(self, move_dmg)
        # --------------
        return (move_name, move_dmg, dmg_message)