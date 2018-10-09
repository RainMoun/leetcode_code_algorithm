class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return list(str(x)) == list(reversed(list(str(x))))

s = Solution()
x = -121
print(s.isPalindrome(x))