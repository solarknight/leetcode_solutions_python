from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, v in enumerate(nums):
            if target - v in d:
                return [d[target - v], i]
            else:
                d[v] = i


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
