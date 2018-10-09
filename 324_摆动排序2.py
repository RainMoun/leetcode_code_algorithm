class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''解法I O(nlogn)时间排序+O(n)空间辅助数组解法：

            1.对原数组排序，得到排序后的辅助数组tmp

            2.对原数组的偶数位下标填充tmp的末尾元素

            3.对原数组的奇数位下标填充tmp的末尾元素
        '''
        nums_sorted = sorted(nums)
        len_nums = len(nums)
        mark_new = 1
        mark_old = len_nums - 1
        while mark_new < len_nums:
            nums[mark_new] = nums_sorted[mark_old]
            mark_old -= 1
            mark_new += 2
        mark_new = 0
        while mark_new < len_nums:
            nums[mark_new] = nums_sorted[mark_old]
            mark_old -= 1
            mark_new += 2
        return nums

class Solution2:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''解法I O(nlogn)时间排序+O(n)空间辅助数组解法：

            1.对原数组排序，得到排序后的辅助数组tmp

            2.对原数组的偶数位下标填充tmp的末尾元素

            3.对原数组的奇数位下标填充tmp的末尾元素
        '''
        nums_sorted = sorted(nums)
        len_nums = len(nums)
        mark_new = 1
        mark_old = len_nums - 1
        while mark_new < len_nums:
            nums[mark_new] = nums_sorted[mark_old]
            mark_old -= 1
            mark_new += 2
        mark_new = 0
        while mark_new < len_nums:
            nums[mark_new] = nums_sorted[mark_old]
            mark_old -= 1
            mark_new += 2
        return nums


s = Solution2()
lst = [1, 5, 1, 1, 6, 4]
print(s.wiggleSort(lst))