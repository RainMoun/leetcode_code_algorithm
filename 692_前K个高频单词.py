from collections import Counter


class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        有问题
        """
        lst_words = Counter(sorted(words)).most_common(k)
        result = []
        for word, _ in lst_words:
            result.append(word)
        return result


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3
s = Solution()
print(s.topKFrequent(words, k))
