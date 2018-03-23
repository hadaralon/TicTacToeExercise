from game_board import GameBoard
from shape_enum import Shapes


def get_coordinates():
    """
    get row/col input
    :return: tuple: coordinate
    """
    x_val = input('Enter row number: ')
    y_val = input('Enter column number: ')
    return x_val, y_val


def main():
    my_board = GameBoard(4)
    check = True
    count = 0
    shape = Shapes(count % 2).name
    print('{0}\'s turn'.format(shape))
    while check:
        my_board.draw_board()
        try:
            coordinates = get_coordinates()
        except IndexError:
            print('Invalid coordinates, please try again.')
    check = True
    while check:
        try:
            game_check = my_board.make_move(shape, coordinates[0], coordinates[1])
            check = False
        except IndexError:
            print('This spot is already taken. Choose a different one.')  # TODO: Check if doesn't interfere with end
            #TODO: of game
    count += 1


main()
