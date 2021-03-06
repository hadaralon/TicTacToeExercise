from shape_enum import Shapes


class GameBoard:
    """
    Board build and operations...
    """

    def __init__(self, size):
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
        self.board_layout = [[' '] * self.size] * self.size

    def __set__(self, x_val, y_val, value):
        """
        sets a shape for a single spot
        :param x_val: ...
        :param y_val: ...
        :param value: shape
        :return:
        """
        self.board_layout[x_val][y_val] = value  # TODO: check how to set property...

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
                board_list[i] = [
                    self.board_layout[int((i - 1) / 2)][int((k - 2) / 4)] if ((k - 2) % 4 == 0) else " " if (k % 4 != 0)
                    else "|" for k in range(4 * self.size + 1)]
                print(*board_list[i])
        return

    def check_board(self, board, x_val, y_val):
        for idx in range(self.size - 2):
            if board[x_val][idx] == board[x_val][idx + 1] == board[x_val][idx + 2]:
                return True
            elif board[idx][y_val] == board[idx + 1][y_val] == board[idx + 2][y_val]:
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

    def make_move(self, shape, x_val, y_val):
        """
        make a move, check for win, then present the right message
        :rtype: object
        :param shape:
        :param x_val:
        :param y_val:
        :return: bool: False if game is over, else True
        """
        if self.board_layout[x_val][y_val] == ' ':
            self.__set__(x_val, y_val, shape)
            self.move_count += 1
            if self.check_board:
                print(Shapes(shape).name + 'Wins!')
                return False
            elif self.move_count == self.size ** 2:
                print('It\'s a draw!')
                return False
            else:
                return True
        else:
            raise IndexError

    def get_coordinates(self):
        """
        get row/col input
        :return: tuple: coordinate
        """
        x_val = int(input('Enter row number: '))
        y_val = int(input('Enter column number: '))
        if not (0 <= x_val < self.size) or not (0 <= y_val < self.size):
            raise IndexError
        if x_val is None or y_val is None:  # TODO: check how to avoid getting None as an input
            raise IndexError
        return x_val, y_val


