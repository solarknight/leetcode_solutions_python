import sys
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        s_nums, sum, cur_shift, min_shift = sorted(nums), 0, 0, sys.maxsize
        for i in range(len(s_nums) - 2):
            left, right = i + 1, len(s_nums) - 1
            while left < right:
                cur_shift = s_nums[left] + s_nums[right] + s_nums[i] - target
                if abs(cur_shift) < min_shift:
                    min_shift = abs(cur_shift)
                    sum = cur_shift + target
                if cur_shift == 0:
                    return target
                elif cur_shift < 0:
                    left += 1
                else:
                    right -= 1
        return sum


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
