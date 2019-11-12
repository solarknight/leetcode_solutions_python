from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_nums, result = sorted(nums), []
        for i in range(len(s_nums) - 2):
            if i != 0 and s_nums[i] == s_nums[i - 1]:
                continue
            left, right = i + 1, len(s_nums) - 1
            while left < right:
                if s_nums[i] + s_nums[left] + s_nums[right] == 0:
                    result.append([s_nums[i], s_nums[left], s_nums[right]])
                    left, right = left + 1, right - 1
                    while left < right and s_nums[left] == s_nums[left - 1]:
                        left += 1
                    while left < right and s_nums[right] == s_nums[right + 1]:
                        right -= 1
                elif s_nums[i] + s_nums[left] + s_nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum([-2, 0, 1, 1, 2]))
