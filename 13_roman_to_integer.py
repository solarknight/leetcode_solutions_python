class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        last, sum = 0, 0
        for i in range(len(s)):
            cur = d[s[i]]
            sum += cur - 2*last if last < cur else cur
            last = cur
        return sum


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("III"))
    print(s.romanToInt("IV"))
    print(s.romanToInt("IX"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV"))
