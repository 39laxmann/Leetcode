class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest_str = min(strs, key= len)

        for i in range(len(shortest_str)):
            for word in strs:
                if word[i] != shortest_str[i]:
                    return shortest_str[:i]

        return shortest_str

        