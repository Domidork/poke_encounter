from functions import *

class pokemon():
    def __init__(self, name):
        self.data = get_pokemon_data('bulbasaur')
        self.possible_moves = get_moves(self.data)
        self.moves = randomize_moves(self.possible_moves)

    def print_stats(self):
        print(f'Health: {self.data['stats'][0]['base_stat']}')
        for move in self.moves:
            print(f'{move['name']}: {move.get('power', 0)}')