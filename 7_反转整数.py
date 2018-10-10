class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        lst_x = list(str(x))
        if str.isdigit(lst_x[0]):
            # print(list(reversed(lst_x[1:])))
            result = int(''.join(list(reversed(lst_x))))
            if result > 2 ** 31 - 1 or result < -(2 ** 31):
                return 0
            else:
                return int(''.join(list(reversed(lst_x))))
        else:
            result = int(''.join([lst_x[0]] + list(reversed(lst_x[1:]))))
            if result > 2 ** 31 - 1 or result < -(2 ** 31):
                return 0
            else:
                return int(''.join([lst_x[0]] + list(reversed(lst_x[1:]))))

s = Solution()
num = 1534236469
print(s.reverse(num))