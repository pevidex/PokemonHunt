from classes import *

matrices_list = []
current_position = None
current_matrix = None
input_ = None
total_pokemons_hunted = 1


def is_command_valid(commands: str) -> bool:
    for character in commands:
        if character != "N" and character != "O" and character != "E" and character != "S":
            return False
    return True


def get_new_position(command: str) -> Position:
    new_position = Position(current_position.x, current_position.y)
    if command == "N":
        new_position.x += 1
    if command == "S":
        new_position.x -= 1
    if command == "E":
        new_position.y += 1
    if command == "O":
        new_position.y -= 1
    return new_position


def process_command(command: str) -> Position:
    global current_position
    global total_pokemons_hunted
    current_position = get_new_position(command)

    if current_matrix.is_position_out_of_limits(current_position):
        #swap_matrixes()
        return
    else:
        if not current_matrix.has_position_been_visited(current_position):
            current_matrix.set_visited_position(current_position)
            total_pokemons_hunted += 1


def init() -> None:
    global total_pokemons_hunted
    total_pokemons_hunted = 1

    global matrices_list
    matrices_list = []

    global current_position
    current_position = None

    global current_matrix
    current_matrix = None

    set_position(Position(0, 0))
    set_initial_matrix()


def set_initial_matrix() -> None:
    matrix = Matrix(-50, 49, -50, 49, [])
    matrices_list.append(matrix)
    set_current_matrix(matrix)


def set_current_matrix(matrix: Matrix) -> None:
    global current_matrix
    current_matrix = matrix
    matrix.build_matrix(input_)
    current_matrix.set_visited_position(current_position)


def set_position(position: Position) -> None:
    global current_position
    current_position = position


def pokemon_hunt() -> None:
    global input_
    input_ = input("Enter your command: ")

    if not is_command_valid(input_):
        print("Bad input")
        return

    init()

    for command in input_:
        process_command(command)
        #print(str(current_position))

    #print("total: " + str(total_pokemons_hunted))
    return total_pokemons_hunted


if __name__ == '__main__':
    pokemon_hunt()
