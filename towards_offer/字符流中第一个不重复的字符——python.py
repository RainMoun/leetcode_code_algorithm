# -*- coding:utf-8 -*-
import collections

class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
    def FirstAppearingOnce(self):
        # write code here
        '''lst_result = list(filter(lambda c: self.s.count(c) == 1, self.s))
        return lst_result[0] if lst_result else '#'''''
        count_char = collections.OrderedDict()
        for i in self.s:
            if i not in count_char.keys():
                count_char[i] = 1
            else:
                del count_char[i]
        return list(count_char.keys())[0] if count_char else '#'

    def Insert(self, char):
        # write code here
        self.s += char


if __name__ == '__main__':
    s = Solution()
    s.Insert('g')
    print(s.FirstAppearingOnce())
    s.Insert('o')
    print(s.FirstAppearingOnce())
    s.Insert('o')
    print(s.FirstAppearingOnce())
    s.Insert('g')
    print(s.FirstAppearingOnce())
    s.Insert('l')
    print(s.FirstAppearingOnce())
    s.Insert('e')
    print(s.FirstAppearingOnce())