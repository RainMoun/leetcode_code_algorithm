class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float 取巧行为
        """
        new_nums = nums1 + nums2
        new_nums = sorted(new_nums)
        key = int(len(new_nums)/2)
        if len(new_nums) % 2 == 0:
            return float((new_nums[key] + new_nums[key-1])/2)
        else:
            return float(new_nums[key])


nums1 = [1, 2]
nums2 = [3, 4]
s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))