import bisect

class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        使用bisect内置模块
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


class KthLargest2:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        保存k个最大元素
        """
        self.k = k
        self.nums = nums
        self.nums = sorted(self.nums, reverse=True)[:self.k]

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) == 0:
            self.nums.append(val)
            return val
        else:
            if val <= self.nums[-1]:
                self.nums.insert(len(self.nums), val)
                return self.nums[self.k-1]
            else:
                count = 0
                for i in self.nums:
                    if val > i:
                        break
                    else:
                        count += 1
                self.nums.insert(count, val)
                self.nums = self.nums[: self.k]
                return self.nums[self.k-1]
# Your KthLargest object will be instantiated and called as such:
k = 2
nums = [0]
kthLargest = KthLargest2(k, nums)
d1 = kthLargest.add(-1)
print(d1)
d2 = kthLargest.add(1)
print(d2)
d3 = kthLargest.add(-2)
print(d3)
d4 = kthLargest.add(-4)
print(d4)
d5 = kthLargest.add(3)
print(d5)
