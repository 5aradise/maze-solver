from window import Window


class Vec2:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def copy(self) -> 'Vec2':
        return Vec2(self.x, self.y)

    def __add__(self, other: 'Vec2') -> 'Vec2':
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vec2') -> 'Vec2':
        return Vec2(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other: 'Vec2') -> 'Vec2':
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"Vec2({self.x}, {self.y})"


class Line:
    def __init__(self, p1: Vec2, p2: Vec2, color: str) -> None:
        self.p1 = p1
        self.p2 = p2
        self.color = color

    def draw(self, win: Window):
        win.canvas.create_line(self.p1.x, self.p1.y,
                               self.p2.x, self.p2.y, fill=self.color, width=2)
