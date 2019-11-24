class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            elif c in mapping:
                stack.append(mapping[c])
            else:
                return False
        return not stack


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("([)]"))
    print(s.isValid("{[]}"))
