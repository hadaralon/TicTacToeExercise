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

    def check_board(self, board):
        """
        checks board layout for win
        TODO: only working on first lineq column- fix it again Tony...
        :param board:
        :return:
        """
        win_check = False
        for i in range(self.size - 2):
            for k in range(self.size - 2):
                if (board[i][k] == board[i][k + 1] and board[i][k + 1] == board[i][k + 2]) and board[i][k] != ' ':
                    win_check = True
                elif (board[i][k] == board[i + 1][k] and board[i + 1][k] == board[i + 2][k]) and board[i][k] != ' ':
                    win_check = True
                elif (board[i][k] == board[i + 1][k + 1] and board[i + 1][k + 1] == board[i + 2][k + 2])\
                        and board[i][k] != ' ':
                    win_check = True
                elif (board[i][k+2] == board[i + 1][k + 1] and board[i + 1][k + 1] == board[i + 2][k])\
                        and board[i][k] != ' ':
                    win_check = True
        return win_check