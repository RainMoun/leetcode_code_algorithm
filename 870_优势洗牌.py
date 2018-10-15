class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        '''初始代码 超出时间限制
        A = sorted(A)
        result = []
        for i in B:
            sign = 0
            for j in A:
                if j > i:
                    result.append(j)
                    A.remove(j)
                    sign = 1
                    break
            if sign == 0:
                result.append(A[0])
                A = A[1:]
        return result
        '''
        A = sorted(A)
        B_sorted = sorted(B)
        count_A = 0
        count = 0
        result = []
        while count_A < len(A):
            while A[0] <= B_sorted[count] and count_A < len(A):
                A.append(A[0])
                A.remove(A[0])
                count_A += 1
            if A[0] > B_sorted[count]:
                result.append(A[0])
                count += 1
                A = A[1:]
        result = result + A
        result_fina = []
        for i in B:
            result_fina.append(result[B_sorted.index(i)])
            B_sorted[B_sorted.index(i)] = None
        return result_fina





A = [2,0,4,1,2]
B = [1,3,0,0,2]

s = Solution()
print(s.advantageCount(A, B))