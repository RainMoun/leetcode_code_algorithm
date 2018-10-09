class Solution:
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = [[]]
        for x in A:
            result.extend([subset + [x] for subset in result])
        sum = 0
        for i in result:
            if len(i) > 0:
                sum += (max(i) - min(i))
        return sum


lst = [2, 1, 3]
s = Solution()
result = s.sumSubseqWidths(lst)
print(result)

