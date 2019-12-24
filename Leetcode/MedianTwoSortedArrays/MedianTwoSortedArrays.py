class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums2) > len(nums1): # swap
            b = nums1
            nums1 = nums2
            nums2 = b
        if (nums1 == []):
            if len(nums2) % 2 == 0:
                return (nums2[int(len(nums2) / 2) - 1] + nums2[int(len(nums2) / 2)]) / 2.0
            if len(nums2) % 2 == 1:
                return nums2[int(len(nums2) / 2)]
        if (nums2 == []):
            if len(nums1) % 2 == 0:
                return (nums1[int(len(nums1) / 2) - 1] + nums1[int(len(nums1) / 2)]) / 2.0
            if len(nums1) % 2 == 1:
                return nums1[int(len(nums1) / 2)]

        total = int((len(nums1) + len(nums2)) / 2)

        nums1_pivot = self.find_nums1_pivot(nums1, nums2, int(len(nums1) / 2), int((len(nums1)-len(nums2))/2), int((len(nums1)+len(nums2))/2))
        nums2_pivot = int((len(nums1) + len(nums2)) / 2) - nums1_pivot
        if nums1_pivot <= 0:
            left_max = nums2[nums2_pivot - 1]
        elif nums2_pivot <= 0:
            left_max = nums1[nums1_pivot - 1]
        else:
            left_max = max(nums1[nums1_pivot - 1], nums2[nums2_pivot - 1])

        if nums1_pivot >= len(nums1):
            right_min = nums2[nums2_pivot]
        elif nums2_pivot >= len(nums2):
            right_min = nums1[nums1_pivot]
        else:
            right_min = min(nums1[nums1_pivot], nums2[nums2_pivot])

        if (len(nums1) + len(nums2)) % 2 == 0:
            return (left_max + right_min) / 2.0
        else:
            return right_min

    def find_nums1_pivot(self, nums1, nums2, nums1_pivot, low, high):
        """
        Recursive method
        Goal: Separate nums1 and nums2 into left and right sub-sections where every element in the left sub-sections is
              smaller than every element in the right sub-sections. We do this by finding a point in nums1, nums1_pivot,
              which separates the nums1 array into left and right sections. Using nums1_pivot, we can find a pivot for
              nums2 since the addition of the lengths of the left sub-section has to equal (or be 1 smaller than if
              the length of arrays is odd) to the right sub-section.
        :param nums1: Larger array
        :param nums2: Smaller array
        :param nums1_pivot: Guess for pivot
        :param low: Lowest possible value for nums1_pivot (used for binary search)
        :param high: Highest possible value for nums1_pivot (used for binary search)
        """
        nums2_pivot = int((len(nums1) + len(nums2)) / 2) - nums1_pivot
        if nums1_pivot <= 0:
            left_max = nums2[nums2_pivot - 1]
            left_flag = False
        elif nums2_pivot <= 0:
            left_max = nums1[nums1_pivot - 1]
            left_flag = True
        else:
            left_max = max(nums1[nums1_pivot - 1], nums2[nums2_pivot - 1])
            if left_max == nums1[nums1_pivot - 1]:
                left_flag = True
            else:
                left_flag = False

        if nums1_pivot >= len(nums1):
            right_min = nums2[nums2_pivot]
        elif nums2_pivot >= len(nums2):
            right_min = nums1[nums1_pivot]
        else:
            right_min = min(nums1[nums1_pivot], nums2[nums2_pivot])

        if left_max <= right_min:
            return nums1_pivot
        else:
            if left_max > right_min:
                if left_flag:  # Go to the left
                    return self.find_nums1_pivot(nums1, nums2, int((low + nums1_pivot) / 2), low, nums1_pivot)
                else:
                    return self.find_nums1_pivot(nums1, nums2, int((nums1_pivot + high) / 2) + 1, nums1_pivot, high)


print(Solution().findMedianSortedArrays([1], [2, 3, 4, 5, 6, 7]))

