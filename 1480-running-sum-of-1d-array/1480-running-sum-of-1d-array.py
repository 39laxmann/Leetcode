class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running = []
        total = 0
        for i in nums:
            total += i
            running.append(total)

        return running