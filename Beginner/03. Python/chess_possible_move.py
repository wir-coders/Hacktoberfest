# Given the piece and its from and to Algebraic notations.
# find if the moment is possible or not

from collections import namedtuple

Square = namedtuple("Square", "File Rank")
Move = namedtuple("Move", "Piece From To")

BOARD = [Square(File = x, Rank = y) for x in "ABCDEFGH" for y in "12345678"]


def move_sep(from_pos: Square, to_pos: Square) -> (int, int):
    return abs(ord(from_pos.File) - ord(to_pos.File)), abs(ord(from_pos.Rank) - ord(to_pos.Rank))


def check_move(move: Move) -> bool:
    if move.Piece not in "RNBQK" or \
            move.From == move.To or \
            move.From not in BOARD or \
            move.To not in BOARD:
        return False

    moved_by = move_sep(move.From, move.To)

    def can_rook_move() -> bool:
        return moved_by[0] == 0 or moved_by[1] == 0

    def can_knight_move() -> bool:
        return moved_by in [(1, 2), (2, 1)]

    def can_bishop_move() -> bool:
        return moved_by[0] == moved_by[1]

    def can_queen_move() -> bool:
        return can_rook_move() or can_bishop_move()

    def can_king_move() -> bool:
        return moved_by in [(0, 1), (1, 0), (1, 1)]


    return {"R": can_rook_move, "N": can_knight_move, "B": can_bishop_move,
            "Q": can_queen_move, "K": can_king_move}[move.Piece]()

#sample input
# print(check_move(Move("Q", Square("D", "2"), Square("D", "4"))))
# print(check_move(Move("K", Square("E", "2"), Square("E", "3"))))
# print(check_move(Move("N", Square("D", "2"), Square("E", "4"))))
# print(check_move(Move("B", Square("D", "2"), Square("F", "4"))))
# print(check_move(Move("R", Square("D", "2"), Square("E", "4"))))
# print(check_move(Move("P", Square("G", "2"), Square("G", "3"))))

#sample output
# True
# True
# True
# True
# False
# False