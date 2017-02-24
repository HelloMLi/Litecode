'''Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321'''
import sys
class Solution(object):
    def reverse(self, x):
        n=abs(x)
        r=0
        while(n>0):
            r=r*10+n%10
            n=n//10
        #if(n>sys.maxsize): return 0
        '''if(x>=0): return  r
        else: return -r'''
        if (x >= 0):
            if (r > 2**31-1):
                return 0
            else:
                return r
        else:
            if(-r<-2**31):
                return 0
            else:
                return -r
'''Inger 占32位二进制位 首位是符号位0表示正数，1表示负数。还剩31位，2的31次方是2147483648
所以最小数是-2147483648
2^n-1到-2^n    31位其中一位是符号位 n=31'''
solution=Solution()
print(solution.reverse(0))
print(2**31)


