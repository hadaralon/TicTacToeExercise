from game_board import GameBoard
from shape_enum import Shapes


def get_coordinates():
    """
    get row/col input
    :return: tuple: coordinate
    """
    xVal = input('Enter row number: ')
    yVal = input('Enter column number: ')
    return xVal, yVal


def main():
    my_board = GameBoard(4)
    check_param = True
    count = 0
    while check_param:
        my_board.draw_board()
        shape = Shapes(count % 2)
        print('{0} shape\'s turn)'.format(shape))
        check_input = True
        while check_input:
            try:
                check_param = my_board.make_move(shape, get_coordinates()[0], get_coordinates()[1])
                check_input = False
            except IndexError:
                print('This spot is already taken. Choose a different one.')  # TODO: Check if doesn't interfere with
                # end of game
        count += 1


main()
