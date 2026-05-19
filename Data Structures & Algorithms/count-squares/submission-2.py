class CountSquares:

    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        result = 0
        px, py = point
        for x, y in self.points.keys():
            if abs(px - x) != abs(py - y) or x == px or y == py:
                continue
            result += self.points[(x, y)] * self.points[(x, py)] * self.points[(px, y)]
        return result


