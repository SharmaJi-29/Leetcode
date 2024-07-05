class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = []
        for i in range(len(nums)) :
            for j in range(i+1,len(nums)):
                if target == nums[i]+nums[j]:
                    a.append(i)
                    a.append(j)
                    break
        return a        
