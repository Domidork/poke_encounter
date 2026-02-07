from functions import *

class pokemon():
    def __init__(self, name):
        self.data = get_pokemon_data(name)
        self.possible_moves = get_moves(self.data)
        self.moves = randomize_moves(self.possible_moves)

    def __str__(self):
        lines = []

        lines.append(f'\n------{self.data['name'].capitalize()}------')
        lines.append(f'Health: {self.data['stats'][0]['base_stat']}')
        lines.append('Moves:')
        
        for move in self.moves:
            lines.append(f'\t{move['name']}: {move.get('power', 0)}')

        lines.append("")

        return '\n'.join(lines)