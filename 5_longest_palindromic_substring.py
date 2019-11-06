class Solution:
    def longestPalindrome(self, s: str) -> str:
        s2 = '^*' + '*'.join(s) + '*$'
        l, right, l_idx, m_idx = [0 for i in range(len(s2))], 0, 0, 0
        for i in range(1, len(s2) - 1):
            l[i] = min(l[2*l_idx - i], right - i) if i < right else 0
            while s2[i - l[i] - 1] == s2[i + l[i] + 1]:
                l[i] += 1
            if i + l[i] > right:
                right = i + l[i]
                l_idx = i
            if l[i] > l[m_idx]:
                m_idx = i
        start = (m_idx - l[m_idx] - 1) // 2
        return s[start:start + l[m_idx]]


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("a"))
    print(s.longestPalindrome("ac"))
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))

# ^*b*a*b*a*d*$
# 0123456789
# ^*c*b*b*d*$
# 0123456789
