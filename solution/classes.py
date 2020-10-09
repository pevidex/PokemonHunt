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


MATRIX_LENGTH = 100


class Matrix:
    positions = None

    def __init__(self, x_start: int, x_end: int, y_start: int, y_end: int,
                 entry_positions: List[EntryPosition]) -> None:
        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end
        self.entry_positions = entry_positions

    def is_position_out_of_limits(self, position: Position) -> bool:
        if position.x > self.x_end or position.y > self.y_end or position.y < self.y_start or position.x < self.x_start:
            return True
        return False

    def reset_positions(self) -> None:
        self.positions = None

    def has_position_been_visited(self, position: Position) -> bool:
        if self.positions[position.x][position.y] == 0:
            return False
        return True

    def set_visited_position(self, position: Position):
        self.positions[position.x][position.y] = 1

    def build_matrix(self, commands: str) -> None:
        self.positions = [[0 for i in range(MATRIX_LENGTH)] for j in range(MATRIX_LENGTH)]
        for entry_position in self.entry_positions:
            for command_index in range(entry_position.command_index, len(commands)):
                if not self.is_position_out_of_limits(entry_position.position):
                    self.positions[entry_position.position.x][entry_position.position.y] = 1
                else:
                    break
        return

