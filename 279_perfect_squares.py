class Solution:
    def numSquares(self, n: int) -> int:
        mem = [0]
        for _ in range(n):
            mem += min(mem[-i*i] for i in range(1, int(len(mem)**(0.5)) + 1)) + 1,
        return mem[n]
