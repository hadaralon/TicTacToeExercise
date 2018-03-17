from game_board import GameBoard


def main():
    my_board = GameBoard(3, [['X', ' ', 'X'],
                             ['X', 'O', 'X'],
                             ['O', 'O', 'X']])
    my_board.draw_board()
    print(my_board.check_board(my_board.board_layout))

main()

