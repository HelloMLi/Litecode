'''Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.'''



class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        ss=''
        i,j=0,0
        maxLength=0
        while(i<n):
            while(j<n):
                if(isPalindromic(s[i:j+1])):
                    if (maxLength < j - i + 1):
                        ss = s[i:j + 1]
                        maxLength=j-i+1
                    #maxLength=max(maxLength,j-i+1)
                    j=j+1
                else:
                    j=j+1
            i=i+1
            j=i
        #return maxLength
        return ss

    def longestPalindrome2(self, s):
        p=[[0 for i in range(0,1000)] for j in range(0,1000)]
        m=len(s)
        maxLength=0
        ss=''
        for i in range(m):
            p[i][i]=1
            maxLength=1
            start=i
        for i in range(m-1):
            if(s[i]==s[i+1]):
                p[i][i+1]=1
                maxLength=2
                start=i
            else:
                p[i][i+1]=0
        for l in range(3,m+1):
            for i in range(0,m-l+1):
                if(p[i+1][i+l-2]==1 and s[i]==s[i+l-1]):
                    p[i][i+l-1]=1
                    start=i
                    maxLength = l
        return s[start:start+maxLength]
        #return maxLength



def isPalindromic(sub):
    n=len(sub)
    if(n==0 or n==1): return True
    elif(sub[0]!=sub[n-1]): return False
    else:
        return isPalindromic(sub[1:n-1])
solution=Solution()
print(solution.longestPalindrome2('babad')) #babad 3,cbbd 2