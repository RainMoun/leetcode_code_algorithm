import bisect

class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        self.nums = sorted(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        count = 0
        for i in self.nums:
            if i <= val:
                break
            else:
                count += 1
        bisect.insort(self.nums, val)
        len_nums = len(self.nums)
        return self.nums[len_nums - self.k]

# Your KthLargest object will be instantiated and called as such:
k = 3
nums = [4,5,8,2]
kthLargest = KthLargest(k, nums)
d1 = kthLargest.add(3)
print(d1)
d2 = kthLargest.add(5)
print(d2)
d3 = kthLargest.add(10)
print(d3)
d4 = kthLargest.add(9)
print(d4)
d5 = kthLargest.add(4)
print(d5)
