class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return False
        t1 = 0
        t2 = 0
        t3 = 0
        ugly_lst = [1]
        while len(ugly_lst) < n:
            ugly_lst.append(min(ugly_lst[t1] * 2, ugly_lst[t2] * 3, ugly_lst[t3] * 5))
            if ugly_lst[-1] == ugly_lst[t1] * 2:
                t1 += 1
            if ugly_lst[-1] == ugly_lst[t2] * 3:
                t2 += 1
            if ugly_lst[-1] == ugly_lst[t3] * 5:
                t3 += 1
        return ugly_lst[-1]



s = Solution()
print(s.nthUglyNumber(256))
