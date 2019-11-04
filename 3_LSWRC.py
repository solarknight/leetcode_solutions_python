class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d, start, max_len = {}, 0, 0
        for i, c in enumerate(s):
            if c in d and start <= d[c]:
                start = d[c] + 1
            else:
                max_len = max(max_len, i - start + 1)
            d[c] = i
        return max_len


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring("abcde"))
    print(s.lengthOfLongestSubstring("aab"))
    print(s.lengthOfLongestSubstring("abb"))
    print(s.lengthOfLongestSubstring("abba"))
