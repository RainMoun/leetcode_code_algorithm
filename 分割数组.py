import time
class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        '''超出时间限制，需要10.31s 18013
        count = 1
        while count <= len(A):
            if max(A[0: count]) <= min(A[count: ]):
                return count
            count += 1
        return len(A)
        '''
        if len(A) == 1:
            return 1
        if len(A) == 0:
            return 0
        if len(A) == 2:
            if A[0] <= A[1]:
                return 1
            else:
                return 2
        max_now = A[0]
        min_now = min(A[1:])
        count = 1
        while count < len(A):
            if A[count - 1] == min_now:
                min_now = min(A[count:])
            max_now = max(max_now, A[count - 1])
            if max_now <= min_now:
                return count
            count += 1
        return len(A)


s = Solution()
lst = [32,57,24,19,0,24,49,67,87,87]
t_1 = time.time()
print(s.partitionDisjoint(lst))
t_2 = time.time()