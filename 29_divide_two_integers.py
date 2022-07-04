class Solution:
    def divide(self, X: int, Y: int) -> int:
        if (X == -2147483648 and Y == -1): return 2147483647
        x, y, res = abs(X), abs(Y), 0
        for i in range(31, -1, -1):
            if x >> i >= y:
                res += 1 << i
                x -= y << i
        return res if (X > 0) == (Y > 0) else -res
