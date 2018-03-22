from shape_enum import Shape


class GameBoard:
    def __init__(self, size, board_layout):
        self.size = size
        if self.size > 0:
            self.okay = True
        else:
            self.okay = False
            raise IndexError
        self.board_layout = board_layout
        # TODO: initialize an empty board....

    def draw_board(self):
        length = (self.size * 2) + 1
        board_list = [0] * length
        for i in range(length):
            if i % 2 == 0:
                board_list[i] = ["-" if (k % 4 != 0) else " " for k in range(4 * self.size)]
                print(*board_list[i])
            else:
                board_list[i] = [" " if (k % 4 != 0) else "|" for k in range(4 * self.size + 1)]
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

    def make_move(self, board, shape, xVal, yVal):
        board[xVal][yVal] = Shape(shape)
        if self.check_board:
            print(Shape(shape) + 'Wins!')
