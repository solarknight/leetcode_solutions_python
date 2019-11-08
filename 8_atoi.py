class Solution:
    def myAtoi(self, str: str) -> int:
        num, sign = 0, None
        for i in range(len(str)):
            if str[i] == ' ' and sign == None:
                continue
            if str[i] >= '0' and str[i] <= '9':
                num = num * 10 + int(str[i])
                if sign == None:
                    sign = True
            elif sign == None and str[i] in ['+', '-']:
                sign = True if str[i] == '+' else False
            else:
                break
        if sign == None or sign == True:
            return num if num <= 2**31 - 1 else 2**31 - 1
        else:
            return -num if num <= 2**31 else -2**31

if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("42"))
    print(s.myAtoi(" +42"))
    print(s.myAtoi(" -42"))
    print(s.myAtoi("4193 with words"))
    print(s.myAtoi("words and 987"))
    print(s.myAtoi("-91283472332"))
    print(s.myAtoi("   +0 123"))
