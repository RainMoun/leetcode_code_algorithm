class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''1.偷懒法
        '''
        return list(sorted(nums, reverse=True))[k-1]


nums = [3, 2, 1, 5, 6, 4]
k = 2
s = Solution()
print(s.findKthLargest(nums, k))
