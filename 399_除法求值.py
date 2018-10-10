class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        "未解决"
        """
        value = {equations[0][0]: 1.0}
        print(value)
        count = 0
        for i in equations:
            if i[0] in value.keys() and i[1] not in value.keys():
                value[i[1]] = value[i[0]] / values[count]
            elif i[0] not in value.keys() and i[1] in value.keys():
                value[i[0]] = value[i[1]] * values[count]
            count += 1
        result = []
        for i in queries:
            if i[0] in value.keys() and i[1] in value.keys():
                result.append(value[i[0]]/value[i[1]])
            else:
                result.append(-1.0)
        return result


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
s = Solution()
print(s.calcEquation(equations, values, queries))