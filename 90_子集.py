class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for x in nums:
            result.extend([subset + [x] for subset in result if subset + [x] not in result])
        return result


s = Solution()
print(s.subsetsWithDup([1,2,2]))