class Solution(object):
    def maxSumDivThree(self, nums):
        total = sum(nums)
        
        # Lists to store small elements by remainder
        rem1 = []
        rem2 = []
        
        for x in nums:
            if x % 3 == 1:
                rem1.append(x)
            elif x % 3 == 2:
                rem2.append(x)
        
        rem1.sort()
        rem2.sort()
        
        if total % 3 == 0:
            return total
        
        # If total % 3 == 1
        if total % 3 == 1:
            option1 = rem1[0] if rem1 else float('inf')
            option2 = sum(rem2[:2]) if len(rem2) >= 2 else float('inf')
            return total - min(option1, option2)
        
        # If total % 3 == 2
        if total % 3 == 2:
            option1 = rem2[0] if rem2 else float('inf')
            option2 = sum(rem1[:2]) if len(rem1) >= 2 else float('inf')
            return total - min(option1, option2)