from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(tmp='', left=0, right=0):
            if len(tmp) == 2 * n:
                ans.append(tmp)
                return
            if left < n:
                backtrack(tmp + '(', left + 1, right)
            if right < left:
                backtrack(tmp + ')', left, right + 1)

        backtrack()
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))
