#Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
'''
For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out=[]
       # index=[]
        '''#超时
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(j>i and -(nums[i]+nums[j]) in nums and nums.index(-(nums[i]+nums[j]))!=i and nums.index(-(nums[i]+nums[j]))!=j):
                    #print([nums[i],nums[j],-(nums[i]+nums[j])])
                    if(sorted([nums[i],nums[j],-(nums[i]+nums[j])]) not in out):
                        #print([nums[i], nums[j], -(nums[i] + nums[j])])
                        out.append(sorted([nums[i],nums[j],-(nums[i]+nums[j])]))
                        #index.append([i,j,nums.index(-(nums[i]+nums[j]))])
                        #print(index)
                        #index.append(sorted([i,j,nums.index(-(nums[i]+nums[j]))]))'''
        s_nums=sorted(nums)  #排好序的数组，寻找两个数的和为指定值 o(n*n)
        for i in range(len(s_nums)):
            find_num=-s_nums[i]
            j=i+1
            k=len(s_nums)-1
            while(j<k):
                if(s_nums[j]+s_nums[k]<find_num):
                    j=j+1
                elif(s_nums[j]+s_nums[k]>find_num):
                    k=k-1
                else:
                    if([s_nums[i],s_nums[j],s_nums[k]] not in out):
                        out.append([s_nums[i],s_nums[j],s_nums[k]])
                    j=j+1
                    k=k-1
        return out

S = [-1, 0, 1, 2, -1, -4]
solution=Solution()
print(solution.threeSum(S))
#print(sorted([-1,-1,2]) in [[-1,0,1],[-1,2,-1]])
#print(S.index(-2))
