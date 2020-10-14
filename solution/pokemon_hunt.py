from classes import Position, Matrix, EntryPosition, get_initial_matrix
import db_service
import os
import psutil

current_position = None
current_matrix = None
input_ = None
input_index = 0
total_pokemons_hunted = 0
matrix_count = 0
cache_matrices = []
MAX_NUMBER_OF_MATRICES_IN_MEMORY = 1000


def is_input_valid(commands: str) -> bool:
    for character in commands:
        if character != "N" and character != "O" and character != "E" and character != "S":
            return False
    return True


def get_new_position(command: str, position: Position) -> Position:
    new_position = Position(position.x, position.y)
    if command == "N":
        new_position.y += 1
    if command == "S":
        new_position.y -= 1
    if command == "E":
        new_position.x += 1
    if command == "O":
        new_position.x -= 1
    return new_position


''' 
Rebuilds matrix based on the array of entry positions and their corresponding input indexes.
'''
def build_matrix(matrix: Matrix) -> None:
    matrix.build_empty_matrix()
    for entry_position in matrix.entry_positions:
        position = None
        start_pointer = -1 if entry_position.command_index == -1 else entry_position.command_index
        for index in range(start_pointer, input_index):
            if position is None:
                position = entry_position.position
            else:
                position = get_new_position(input_[index], position)
            if matrix.is_position_out_of_limits(position):
                break
            else:
                matrix.set_visited_position(position)


def get_matrix_from_db(position: Position) -> Matrix:
    return db_service.get_matrix_containing_position(position)


def translate_matrix_based_on_command(command: str, matrix: Matrix) -> None:
    if command == "O":
        matrix.translate_O()
    elif command == "E":
        matrix.translate_E()
    elif command == "N":
        matrix.translate_N()
    elif command == "S":
        matrix.translate_S()


def pop_matrix() -> None:
    db_service.save_matrix(cache_matrices[0])
    del cache_matrices[0]


def generate_matrix(command: str) -> Matrix:
    global matrix_count

    if len(cache_matrices) == MAX_NUMBER_OF_MATRICES_IN_MEMORY:
        pop_matrix()

    matrix = Matrix(matrix_count, current_matrix.x_start, current_matrix.x_end, current_matrix.y_start,
                    current_matrix.y_end,
                    [EntryPosition(current_position, input_index)])

    translate_matrix_based_on_command(command, matrix)
    matrix_count += 1
    cache_matrices.append(matrix)
    return matrix


def get_matrix_from_cache(position: Position, push_to_top: True) -> Matrix:
    for matrix_index in range(len(cache_matrices)):
        if not cache_matrices[matrix_index].is_position_out_of_limits(position):
            matrix = cache_matrices[matrix_index]
            if push_to_top:
                cache_matrices.append(matrix)
                del cache_matrices[matrix_index]
            return matrix
    return None


def add_new_entry_position_to_matrix(matrix: Matrix) -> None:
    global current_position

    entry_position = EntryPosition(current_position, input_index)
    matrix.add_new_entry_position(entry_position)


def visit_house() -> None:
    if not current_matrix.has_position_been_visited(current_position):
        current_matrix.set_visited_position(current_position)
        increment_total_pokemons()


def swap_matrixes(command: str) -> None:
    global current_position

    matrix = get_matrix_from_cache(current_position, True)

    if matrix is not None:
        set_current_matrix(matrix)
        visit_house()
        add_new_entry_position_to_matrix(matrix)
        return

    matrix = get_matrix_from_db(current_position)

    if matrix is None:
        matrix = generate_matrix(command)
    else:
        build_matrix(matrix)
        add_new_entry_position_to_matrix(matrix)
        cache_matrices.append(matrix)
    set_current_matrix(matrix)
    visit_house()


def process_command(command: str) -> None:
    global current_position
    current_position = get_new_position(command, current_position)

    if current_matrix.is_position_out_of_limits(current_position):
        swap_matrixes(command)
    elif not current_matrix.has_position_been_visited(current_position):
        current_matrix.set_visited_position(current_position)
        increment_total_pokemons()


def init() -> None:
    global total_pokemons_hunted
    total_pokemons_hunted = 0

    db_service.init()

    global cache_matrices
    cache_matrices = []

    global matrix_count
    matrix_count = 0

    global current_position
    current_position = None

    global current_matrix
    current_matrix = None

    global input_index
    input_index = 0

    set_position(Position(0, 0))
    set_initial_matrix()


def set_initial_matrix() -> None:
    global input_index
    global current_matrix
    global matrix_count

    matrix = get_initial_matrix(current_position)
    matrix_count += 1
    matrix.set_visited_position(current_position)
    increment_total_pokemons()

    cache_matrices.append(matrix)
    current_matrix = matrix


def set_current_matrix(matrix: Matrix) -> None:
    global current_matrix
    current_matrix = matrix


def increment_total_pokemons() -> None:
    global total_pokemons_hunted
    total_pokemons_hunted += 1


def set_position(position: Position) -> None:
    global current_position
    current_position = position


def print_state() -> None:
    print("current state after command " + input_[input_index] + " (" + str(input_index) + ")")
    print("total pokemons: " + str(total_pokemons_hunted))
    print("position: " + str(current_position))
    print("matrix:\n" + str(current_matrix) + "\n")


def pokemon_hunt() -> None:
    global input_
    global input_index
    input_ = input("Enter your list of commands: ")

    # file = open("../inputs/input6.txt", "r")
    # input_ = file.read()

    if not is_input_valid(input_):
        print("Bad input")
        return -1

    init()

    for input_index in range(len(input_)):
        process_command(input_[input_index])
        #print_state()

    # process = psutil.Process(os.getpid())
    # print(process.memory_info().rss)

    db_service.close_connection()

    print("total: " + str(total_pokemons_hunted))
    return total_pokemons_hunted


if __name__ == '__main__':
    pokemon_hunt()
