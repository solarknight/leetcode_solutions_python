from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        max_str, min_str = max(strs), min(strs)
        max_len = min(len(max_str), len(min_str))
        for i in range(max_len + 1):
            if i == max_len or max_str[i] != min_str[i]:
                break
        return min_str[0:i]


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
    print(s.longestCommonPrefix(["", ""]))
    print(s.longestCommonPrefix(["c", "c"]))
