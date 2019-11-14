from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        d = {2: "abc", 3: "def", 4: "ghi", 5: "jkl",
             6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        result = [""]
        for c in digits:
            i, tmp_result = int(c), []
            for s in d[i]:
                for res in result:
                    tmp_result.append(res + s)
            result = tmp_result
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))
