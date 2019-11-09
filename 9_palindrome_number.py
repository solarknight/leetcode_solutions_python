class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        origin, reversed = x, 0
        while origin != 0:
            origin, reversed = origin // 10, 10 * reversed + origin % 10
        return x == reversed


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(10))

