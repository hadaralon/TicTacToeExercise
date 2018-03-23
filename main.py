from game_board import GameBoard
from shape_enum import Shapes


def main():
    my_board = GameBoard(4)
    check = True
    game_check = True
    count = 0
    while game_check:
        shape = Shapes(count % 2).name
        print('{0}\'s turn'.format(shape))
        while check:
            my_board.draw_board()
            try:
                coordinates = my_board.get_coordinates()
            except IndexError:
                print('Invalid coordinates, please try again.')
        check = True
        while check:
            try:
                my_board.make_move(shape, coordinates[0], coordinates[1])
                game_check = my_board.make_move(shape, coordinates[0], coordinates[1])
                check = False
            except IndexError:
                print('This spot is already taken. Choose a different one.')  # TODO: Check if doesn't interfere with
                # TODO: end of game
        count += 1


main()
