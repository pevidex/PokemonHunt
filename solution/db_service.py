import pymongo
from classes import Matrix, EntryPosition, Position


my_client = None
my_db = None
matrices = None


def init() -> None:
    global my_client
    global my_db
    global matrices

    my_client = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = my_client["premium_minds_db"]

    reset_tables()

    matrices = my_db["matrices"]


def reset_tables() -> None:
    global matrices
    matrices = my_db["matrices"]
    if matrices is not None:
        matrices.drop()


def save_matrix(matrix: Matrix) -> None:
    matrix = {"id": matrix.id, "x_start": matrix.x_start, "x_end": matrix.x_end, "y_start": matrix.y_start,
              "y_end": matrix.y_end, "entry_positions": [entry.as_dict() for entry in matrix.entry_positions]}

    x = matrices.update_one({'id':matrix['id']}, matrix, True)


def get_matrix_containing_position(position: Position) -> Matrix:
    query = {"x_start": {"$lte": position.x}, "x_end": {"$gte": position.x}, "y_start": {"$lte": position.y},
             "y_end": {"$gte": position.y}}

    matrix = matrices.find_one(query)

    if matrix is None:
        return None

    return Matrix(matrix["id"], matrix["x_start"], matrix["x_end"], matrix["y_start"], matrix["y_end"],
                  [EntryPosition(Position(entry["x"], entry["y"]), entry["command_index"]) for entry in
                   matrix["entry_positions"]])


def register_new_entry_position(matrix: Matrix, entry_position: EntryPosition) -> None:
    my_query = {"id": matrix.id}
    new_entry_position = {"$push": {"entry_positions": entry_position.as_dict()}}

    matrices.update_one(my_query, new_entry_position)


def close_connection() -> None:
    global my_client
    global my_db

    reset_tables()

    my_client = None
    my_db = None


if __name__ == '__main__':
    init()
