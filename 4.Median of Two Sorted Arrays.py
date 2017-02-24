'''There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums=[]
        nums1_length=len(nums1)
        nums2_length=len(nums2)
        i,j,k=0,0,0
        while(i<nums1_length and j<nums2_length):
            if(nums1[i]<nums2[j]):
                nums.append(nums1[i])
                k=k+1
                i=i+1
            else:
                nums.append(nums2[j])
                k=k+1
                j=j+1
        while(i<nums1_length):
            nums.append(nums1[i])
            i=i+1
            k=k+1
        while(j<nums2_length):
            nums.append(nums2[j])
            j=j+1
            k = k + 1
        #print('k',k)
        #for i in nums:
            #print('nums',i)
        if(k%2==1): return nums[k//2+1-1]
        else:
            print(nums[k / 2 - 1], nums[k / 2 + 1 - 1], (nums[k / 2 - 1] +nums[k / 2 + 1 - 1]) / 2)
            return (nums[k//2-1]+nums[k//2+1-1])/2
        #return nums
nums1 = [1,2]
nums2 = [3,4]
solution=Solution()
middle=solution.findMedianSortedArrays(nums1,nums2)
print(middle)