from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)
        lbound, rbound, half_len = 0, len1, (len1 + len2 + 1) // 2
        while lbound <= rbound:
            count1 = lbound + (rbound - lbound) // 2
            count2 = half_len - count1
            if count1 > 0 and nums1[count1 - 1]  > nums2[count2]:
                rbound = count1 - 1
            elif count1 < len1 and nums2[count2 - 1] > nums1[count1]:
                lbound = count1 + 1
            else:
                left_half = nums2[count2 - 1] if count1 == 0 else nums1[count1 - 1] if count2 == 0 else max(nums1[count1 - 1], nums2[count2 - 1])
                if (len1 + len2) & 1:
                    return left_half
                right_half = nums2[count2] if count1 == len1 else nums1[count1] if count2 == len2 else min(nums1[count1], nums2[count2])
                return (left_half + right_half) / 2
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1, 3], [2]))
    print(s.findMedianSortedArrays([1, 3, 5, 7], [10, 12, 15, 18]))
