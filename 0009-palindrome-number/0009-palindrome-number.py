class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        sum = 0
        while x > 0:
            rem = x % 10
            sum = sum * 10 + rem
            x //= 10
        if sum == temp:
            return True
        else:
            return False