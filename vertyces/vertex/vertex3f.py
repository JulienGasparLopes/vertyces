class Vertex3f:
    _x: float
    _y: float
    _z: float

    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        self._x = x
        self._y = y
        self._z = z

    def clone(self) -> "Vertex3f":
        return Vertex3f(self.x, self.y, self.z)

    def translated(self, v: "Vertex3f") -> "Vertex3f":
        return Vertex3f(self.x + v.x, self.y + v.y, self.z + v.z)

    def multiplied(self, mult: float) -> "Vertex3f":
        return Vertex3f(self.x * mult, self.y * mult, self.z * mult)

    def divided(self, div: float) -> "Vertex3f":
        return Vertex3f(self._x / div, self._y / div, self._z / div)

    def floored(self) -> "Vertex3f":
        return Vertex3f(self._x // 1, self._y // 1, self._z // 1)

    def ceiled(self) -> "Vertex3f":
        return Vertex3f(self._x // 1 + 1, self._y // 1 + 1, self._z // 1 + 1)

    def inverted(self) -> "Vertex3f":
        return Vertex3f(-self._x, -self._y, -self._z)

    def normalized(self) -> "Vertex3f":
        norm = self.norm
        return Vertex3f(self._x / norm, self._y / norm, self._z / norm)

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def z(self) -> float:
        return self._z

    @property
    def norm(self) -> float:
        return (self._x**2 + self._y**2 + self._z**2) ** 0.5

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vertex3f):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))
