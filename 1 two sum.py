#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Given nums = [2, 7, 11, 15], target = 9,Because nums[0] + nums[1] = 2 + 7 = 9,return [0, 1].

class Solution(object):
    def twoSum(self,nums,target):
        '''#超时
        indices=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(j!=i and (target-nums[i])==nums[j]):
                    indices.append(i)
                    indices.append(j)
                    return indices'''
        indices = []
        for i in range(len(nums)):
            if ((target - nums[i]) in nums and nums.index(target - nums[i])!=i):
                indices.append(i)
                indices.append(nums.index(target - nums[i]))
                return indices
solution=Solution()
print(solution.twoSum(nums=[3,2,4],target=7))