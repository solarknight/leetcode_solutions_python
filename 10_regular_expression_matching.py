class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(p)):
            dp[0][i + 1] = p[i] == '*' and dp[0][i - 1]
        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == s[i]:
                    dp[i + 1][j + 1] = dp[i][j]
                if p[j] == '.':
                    dp[i + 1][j + 1] = dp[i][j]
                if p[j] == '*':
                    if p[j - 1] != s[i] and p[j - 1] != '.':
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    else:
                        dp[i + 1][j + 1] = dp[i + 1][j - 1] or dp[i + 1][j] or dp[i][j + 1]
        return dp[len(s)][len(p)]



if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("aa", "a"))
    print(s.isMatch("aa", "a*"))
    print(s.isMatch("ab", ".*"))
    print(s.isMatch("aab", "c*a*b"))
    print(s.isMatch("mississippi", "mis*is*p*."))
