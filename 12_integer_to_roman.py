class Solution:
    def intToRoman(self, num: int) -> str:
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        if num < 10:
            return I[num]
        elif num < 100:
            return X[num//10] + I[num % 10]
        elif num < 1000:
            return C[num//100] + X[(num % 100)//10] + I[num % 10]
        else:
            return M[num//1000] + C[(num % 1000)//100] + X[(num % 100)//10] + I[num % 10]


if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(3))
    print(s.intToRoman(4))
    print(s.intToRoman(9))
    print(s.intToRoman(58))
    print(s.intToRoman(1994))
