from unittest import TestCase, main
from mock import patch
from ..PokemonHunt import pokemon_hunt

class SingleMatrixTest(TestCase):

    def test_no_input(self):
        with patch('builtins.input', return_value='') as _raw_input:
            self.assertEqual(PokemonHunt.pokemon_hunt(), 1)

    def test_circular_path(self):
        with patch('builtins.input', return_value='NESO') as _raw_input:
            self.assertEqual(PokemonHunt.pokemon_hunt(), 4)

    def test_no_repeated_houses(self):
        with patch('builtins.input', return_value='NNNOOOOSS') as _raw_input:
            self.assertEqual(PokemonHunt.pokemon_hunt(), 10)

    def test_repeated_houses(self):
        with patch('builtins.input', return_value='NSNSNSNSNSN') as _raw_input:
            self.assertEqual(PokemonHunt.pokemon_hunt(), 2)


if __name__ == '__main__':
    main()