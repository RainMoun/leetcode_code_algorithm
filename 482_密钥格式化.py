class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        '''超时做法lst = list(S)
        while '-' in lst:
            lst.remove('-')
        len_str = len(lst)
        num_1 = int(len_str - (int(len_str / K)) * K)
        result_lst = lst[0: num_1]
        for i in range(int(len_str / K)):
            if len(result_lst) != 0:
                result_lst.append('-')
            result_lst.extend(lst[num_1 + i * K: num_1 + i * K + K])
        result_str = ''.join(result_lst)
        return result_str.upper()'''
        '''while '-' in lst:
            lst.remove('-')'''
        # 不超时做法
        S = filter(lambda x: x is not '-', S)
        lst = list(S)
        len_str = len(lst)
        num_d = int(len_str / K)
        num_1 = int(len_str - num_d * K)
        if num_1 == 0:
            for i in range(num_d - 1):
                lst.insert((i + 1) * K + i, '-')
        else:
            for i in range(num_d):
                lst.insert(num_1 + i * K + i, '-')
        return ''.join(lst).upper()


S = "5F3Z-2e-9-w"
K = 4
s = Solution()
print(s.licenseKeyFormatting(S, K))
print(str.isalpha('12A'))
