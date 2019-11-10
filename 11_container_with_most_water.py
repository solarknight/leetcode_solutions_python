from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area, i, j = 0, 0, len(height) - 1
        while i < j:
            area = max(area, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1, 2]))
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
