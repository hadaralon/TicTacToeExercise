from shape_enum import Shapes


class GameBoard:
    """
    Board build and operations...
    """
    def __init__(self, size, ):
        """
        :rtype: object
        :param size: int, presents N in NxN list.
        """
        self.move_count = 0
        self.size = size
        if self.size > 0:
            self.okay = True
        else:
            self.okay = False
            raise IndexError
        self.board_layout = [['1'] * self.size] * self.size

    def draw_board(self):
        """
        print current board layout.
        :return: None
        """
        length = (self.size * 2) + 1
        board_list = [0] * length
        for i in range(length):
            if i % 2 == 0:
                board_list[i] = ["-" if (k % 4 != 0) else " " for k in range(4 * self.size)]
                print(*board_list[i])
            else:
                board_list[i] = [self.board_layout[i][k / 2] if (k % 2 == 0) else " " if (k % 4 != 0) else "|" for k in
                                 range(4 * self.size + 1)]  # TODO: k/2 shit
                print(*board_list[i])
        return

    def check_board(self, board, xVal, yVal):
        """
        checks board layout for win
        TODO: only working on first line column- fix it again Tony...
        :param board:
        :return:
        """
        for idx in range(self.size - 2):
            if board[xVal][idx] == board[xVal][idx + 1] == board[xVal][idx + 2]:
                return True
            elif board[idx][yVal] == board[idx + 1][yVal] == board[idx + 2][yVal]:
                return True
        # xy_diff = xVal - yVal
        # for x in range(self.size - 2):
        #     for y in range(self.size - 2):
        #         if x - y == xy_diff:
        #             try:
        #
        #             except:
        #                 pass
        #
        # xy_sum = xVal + yVal

    def make_move(self, shape, xVal, yVal):
        """
        make a move, check for win, then present the right message
        :rtype: object
        :param shape:
        :param xVal:
        :param yVal:
        :return: bool: False if game is over, else True
        """
        if self.board_layout[xVal][yVal] is ' ':
            self.board_layout[xVal][yVal] = Shapes(shape)
            self.move_count += 1
            if self.check_board:
                print(Shapes(shape) + 'Wins!')
                return False
            elif self.move_count == self.size ** 2:
                print('It\'s a draw!')
                return False
            else:
                return True
        else:
            raise IndexError
