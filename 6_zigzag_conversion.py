class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        slot, idx = ["" for i in range(numRows)], 0
        for i in range(len(s)):
            slot[idx] += s[i]
            if idx == 0:
                incr = 1
            if idx == numRows - 1:
                incr = -1
            idx += incr
        return ''.join(slot)


if __name__ == "__main__":
    s = Solution()
    print(s.convert("", 1))
    print(s.convert("a", 2))
    print(s.convert("PAYPALISHIRING", 3))
