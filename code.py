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

letters = ["", "X", "O"]

def reset_scores():
    global x_wins, o_wins
    x_wins = 0
    o_wins = 0

def reset_board():
    global game_on, x_is_next, tiles, tile_letters
    tiles = [""] * 9
    tile_letters = [""] * 9
    game_on = True
    x_is_next = True

def check_endgame():
    global x_wins, o_wins
    for combination in winning_combinations:
        a, b, c = combination
        if tile_letters[a] == tile_letters[b] == tile_letters[c] != letters[0]:
            winner = tiles[a]
            message = f"{winner} wins!"
            if winner == letters[1]:
                x_wins += 1
            else:
                o_wins += 1
            return message
    if all(cell != "" for cell in tiles):
        return "It's a draw!"
    return None

def setup():
    global game_on
    game_on = True

def click(index):
    global game_on, x_is_next
    if not game_on:
        return
    if tiles[index] != "":
        return
    letter = letters[1] if x_is_next else letters[2]
    tile_letters[index] = letter
    tiles[index] = letter
    x_is_next = not x_is_next
    endgame_result = check_endgame()
    if endgame_result:
        game_on = False
        return endgame_result

def reset():
    reset_board()
    setup()

reset_scores()
reset_board()
