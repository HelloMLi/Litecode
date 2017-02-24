'''Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        if(n>0):max_length=1
        else:
            max_length=0
            return max_length
        for i in range(n):
            for j in range(i+1,n):
                #print(i,j)
                unrepeat=1
                sub=s[i:j+1]
                #print(sub)
                for m in range(i,j+1):
                    #print('sm',s[m])
                    #print(s.find(s[m],i,j+1))
                    #print(s.rfind(s[m],i,j+1))
                    if(s.find(s[m],i,j+1)!=s.rfind(s[m],i,j+1)):
                        unrepeat=0
                        break
                #print('unrepeat',unrepeat)
                if(unrepeat==1 and j-i+1>max_length):
                    max_length=j-i+1
                    s_sub=sub
        return max_length
        #return  s_sub
    def lengthOfLongestSubstring2(self,s):
       n=len(s)
       i,j=0,0
       max_length=0
       while i<n:
           hs=set()
           while j<n:
               if(s[j] not in hs):
                   hs.add(s[j])
                   max_length = max(max_length, j + 1 - i)
                   j=j+1
               else:
                   break
           i=i+1
           j=i

       return max_length


       ''' n=len(s)
        hs=set()
        max_length=0
        i,j=0,0
        while(i<n and j<n):
            if(s[j] not in hs):
                hs.add(s[j])
                max_length=max(max_length,j+1-i)
                j=j+1
            else:
                hs.remove(s[i])
                i = i + 1
        return max_length'''





'''info='abcadef'
print(info.find('a',0,3))
print(info.rfind('a',0,3))
print(info[0:4])'''
solution=Solution()
print(solution.lengthOfLongestSubstring2('bbbbb'))#abcabcbb 3, bbbbb 1,pwwkew 3