class GameBoard:
    def __init__(self, size):
        self.size = size
        if self.size > 0:
            self.okay = True
        else:
            self.okay = False
            raise IndexError

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

    # def check_board(self, board):
    #     win_check = False
    #     for i in range(self.size):
    #         for k in range(self.size):
    #             if board[]
