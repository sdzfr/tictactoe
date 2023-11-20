from random import shuffle

tiles = [""] * 9
tile_letters = [""] * 9
x_wins = 0
o_wins = 0
x_is_next = True
game_on = False

winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

