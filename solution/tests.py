from unittest import TestCase, main
from mock import patch
import pokemon_hunt
import classes


class SingleMatrixTest(TestCase):

	def test_bad_input(self):
		with patch('builtins.input', return_value='A-9') as _raw_input:
			self.assertEqual(pokemon_hunt.pokemon_hunt(), -1)

	def test_no_input(self):
		with patch('builtins.input', return_value='') as _raw_input:
			self.assertEqual(pokemon_hunt.pokemon_hunt(), 1)

	def test_circular_path(self):
		with patch('builtins.input', return_value='NESO') as _raw_input:
			self.assertEqual(pokemon_hunt.pokemon_hunt(), 4)

	def test_no_repeated_houses(self):
		with patch('builtins.input', return_value='NNNOOOSS') as _raw_input:
			self.assertEqual(pokemon_hunt.pokemon_hunt(), 9)

	def test_repeated_houses(self):
		with patch('builtins.input', return_value='NSNSNSNSNSN') as _raw_input:
			self.assertEqual(pokemon_hunt.pokemon_hunt(), 2)


class DoubleMatrixTest(TestCase):

	def test_straight_line(self):
		input = classes.MATRIX_LENGTH * "N"
		with patch('builtins.input', return_value=input) as _raw_input:
			self.assertEqual(pokemon_hunt.pokemon_hunt(), classes.MATRIX_LENGTH+1)

	def test_comeback_to_initial_matrix(self):
		input = classes.MATRIX_LENGTH * "N" + classes.MATRIX_LENGTH * "S"
		with patch('builtins.input', return_value=input) as _raw_input:
			self.assertEqual(pokemon_hunt.pokemon_hunt(), classes.MATRIX_LENGTH+1)

	def test_multiple_comebacks(self):
		input = classes.MATRIX_LENGTH * "N" + classes.MATRIX_LENGTH * "S" + classes.MATRIX_LENGTH * "N" + classes.MATRIX_LENGTH * "S" + classes.MATRIX_LENGTH * "N"
		with patch('builtins.input', return_value=input) as _raw_input:
			self.assertEqual(pokemon_hunt.pokemon_hunt(), classes.MATRIX_LENGTH+1)

	def test_negative_values(self):
		with patch('builtins.input', return_value="SESOEESEOOSENSOESOSOONEENSN") as _raw_input:
			self.assertEqual(pokemon_hunt.pokemon_hunt(), 18)


class MultipleMatricesTest(TestCase):
	def test_circular_matrices(self):
		input = classes.MATRIX_LENGTH * "N" + classes.MATRIX_LENGTH * "E" + classes.MATRIX_LENGTH * "S" + classes.MATRIX_LENGTH * "O"
		with patch('builtins.input',
				   return_value=input) as _raw_input:
			self.assertEqual(pokemon_hunt.pokemon_hunt(), 4*classes.MATRIX_LENGTH)

class LargeInputTest(TestCase):
	def test_large_input_1(self):
		inputFile = open("../inputs/input1.txt", "r")
		input = inputFile.read()
		inputFile.close()
		with patch('builtins.input',
				   return_value=input) as _raw_input:
			self.assertEqual(pokemon_hunt.pokemon_hunt(), 10001)

	def test_large_input_2(self):
		inputFile = open("../inputs/input2.txt", "r")
		input = inputFile.read()
		inputFile.close()
		with patch('builtins.input',
				   return_value=input) as _raw_input:
			self.assertEqual(pokemon_hunt.pokemon_hunt(), 21768)

	def test_large_input_3(self):
		inputFile = open("../inputs/input3.txt", "r")
		input = inputFile.read()
		inputFile.close()
		with patch('builtins.input',
				   return_value=input) as _raw_input:
			self.assertEqual(pokemon_hunt.pokemon_hunt(), 59001)

	def test_large_input_4(self):
		inputFile = open("../inputs/input4.txt", "r")
		input = inputFile.read()
		inputFile.close()
		with patch('builtins.input',
				   return_value=input) as _raw_input:
			self.assertEqual(pokemon_hunt.pokemon_hunt(), 162985)

	def test_large_input_5(self):
		inputFile = open("../inputs/input5.txt", "r")
		input = inputFile.read()
		inputFile.close()
		with patch('builtins.input',
				   return_value=input) as _raw_input:
			self.assertEqual(pokemon_hunt.pokemon_hunt(), 1670278)


if __name__ == '__main__':
	main()
