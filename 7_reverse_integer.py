class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            return -self.reverse(-x)
        reversed = int(str(x)[::-1])
        return reversed if reversed >= -(2**31) and reversed <= 2**31 - 1 else 0


if __name__ == "__main__":
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(120))
    print(s.reverse(1534236469))
