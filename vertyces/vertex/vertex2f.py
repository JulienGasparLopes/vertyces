class Vertex2f:
    _x: float
    _y: float

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self._x = x
        self._y = y

    def clone(self) -> "Vertex2f":
        return Vertex2f(self._x, self._y)

    def translated(self, v: "Vertex2f") -> "Vertex2f":
        return Vertex2f(self._x + v._x, self._y + v._y)

    def multiplied(self, mult: float) -> "Vertex2f":
        return Vertex2f(self._x * mult, self._y * mult)

    def divided(self, div: float) -> "Vertex2f":
        return Vertex2f(self._x / div, self._y / div)

    def floored(self) -> "Vertex2f":
        return Vertex2f(self._x // 1, self._y // 1)

    def ceiled(self) -> "Vertex2f":
        return Vertex2f(self._x // 1 + 1, self._y // 1 + 1)

    def inverted(self) -> "Vertex2f":
        return Vertex2f(-self._x, -self._y)

    def normalized(self) -> "Vertex2f":
        norm = self.norm
        return Vertex2f(self._x / norm, self._y / norm)

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def norm(self) -> float:
        return (self._x**2 + self._y**2) ** 0.5

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vertex2f):
            return self._x == other._x and self._y == other._y
        return False

    def __hash__(self) -> int:
        return hash((self._x, self._y))
