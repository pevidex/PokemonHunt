from typing import List


class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def is_equal(self, position) -> bool:
        if position.x == self.x and position.y == self.y:
            return True
        return False

    def __str__(self) -> str:
        return "(" + str(self.x) + "," + str(self.y) + ")"


class EntryPosition:

    def __init__(self, position: Position, command_index: int) -> None:
        self.position = position
        self.command_index = command_index

    def as_dict(self) -> dict:
        return {"x" : self.position.x, "y" : self.position.y, "command_index" : self.command_index}


MATRIX_LENGTH = 50

class Matrix:
    positions = None

    def __init__(self, id: int ,x_start: int, x_end: int, y_start: int, y_end: int,
                 entry_positions: List[EntryPosition]) -> None:
        self.id = id
        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end
        self.entry_positions = entry_positions
        self.build_empty_matrix()

    def is_position_out_of_limits(self, position: Position) -> bool:
        if position.x > self.x_end or position.y > self.y_end or position.y < self.y_start or position.x < self.x_start:
            return True
        return False

    def add_new_entry_position(self, entry_position: EntryPosition) -> None:
        self.entry_positions.append(entry_position)

    def reset_positions(self) -> None:
        self.positions = None

    def has_position_been_visited(self, position: Position) -> bool:
        if self.positions[self.get_local_x(position)][self.get_local_y(position)] == 0:
            return False
        return True

    def get_local_x(self, position: Position) -> int:
        return position.x - self.x_start

    def get_local_y(self, position: Position) -> int:
        return position.y - self.y_start

    def set_visited_position(self, position: Position):
        self.positions[self.get_local_x(position)][self.get_local_y(position)] = 1

    def build_empty_matrix(self):
        self.positions = [[0 for i in range(MATRIX_LENGTH)] for j in range(MATRIX_LENGTH)]

    def translate_O(self):
        self.x_end -= MATRIX_LENGTH
        self.x_start -= MATRIX_LENGTH

    def translate_E(self):
        self.x_end += MATRIX_LENGTH
        self.x_start += MATRIX_LENGTH

    def translate_N(self):
        self.y_end += MATRIX_LENGTH
        self.y_start += MATRIX_LENGTH

    def translate_S(self):
        self.y_end -= MATRIX_LENGTH
        self.y_start -= MATRIX_LENGTH

    def __str__(self) -> str:
        return "x -> " + str(self.x_start) + ":" + str(self.x_end) + "\n" + "y -> " + str(self.y_start) + ":" + str(self.y_end)


def get_initial_matrix(position: Position) -> Matrix:
    entry_position = EntryPosition(position, -1)

    x_start = int( - MATRIX_LENGTH / 2)
    x_end = int(MATRIX_LENGTH / 2 - 1)
    y_start = int(- MATRIX_LENGTH / 2)
    y_end = int(MATRIX_LENGTH / 2 - 1)

    matrix = Matrix(0, x_start, x_end, y_start, y_end, [entry_position])

    return matrix