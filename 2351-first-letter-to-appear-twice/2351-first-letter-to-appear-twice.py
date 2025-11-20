class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        index_dict = {}
        min_second_index = float('inf')
        
        for i, char in enumerate(s):
            if char in index_dict:
                if i < min_second_index:
                    min_second_index = i
                    result = char
            else:
                index_dict[char] = i
        return result