import window
import graphics


class Cell:
    def __init__(self, win: window.Window,
                 top_left: graphics.Vec2, bot_right: graphics.Vec2,
                 has_left_wall=False,
                 has_right_wall=False,
                 has_top_wall=False,
                 has_bottom_wall=False) -> None:
        self.l_wall = has_left_wall
        self.r_wall = has_right_wall
        self.t_wall = has_top_wall
        self.b_wall = has_bottom_wall
        self._tl = top_left
        self._br = bot_right
        self._win = win

    def draw(self):
        pass
