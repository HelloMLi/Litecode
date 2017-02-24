'''
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution(object):
    def reverse(self,l1):     #以循环的方式逆序输出链表
        if(l1==None): return None
        cur=l1
        pre=None
        temp=l1.next
        cur.next=pre
        while(temp!=None):
            pre=cur
            cur=temp
            temp=cur.next
            cur.next=pre
        print('cur',cur.val)
        return cur
    def printList(self,p):
        while (p != None):
            print(p.val)
            p = p.next
    def addTwoNumbers(self,l1,l2):
        resultList=ListNode(0)
        rl=resultList
        p=l1
        q=l2
        carry=0
        while(p!=None or q!=None):
            if(p!=None):
                x=p.val
            else:
                x=0
            print('x',x)
            y=(q.val if q!=None else 0)    #代替Java的 ？：条件运算符
            print('y',y)
            ln_num=(x+y+carry)%10
            carry=(x+y+carry)//10          #python2中 /为整除，Python3中 /为浮点除  //为整除。Python中 ** 为指数
            print('carry',carry)
            print('node',ln_num)
            rl.next=ListNode(ln_num)
            rl=rl.next
            if(p!=None): p=p.next
            if(q!=None): q=q.next
        if (carry == 1): rl.next = ListNode(carry)  #对于[5],[5]  结果为【1，0】. 用于最后还有carry的
        return resultList.next



'''l1=ListNode(2)
temp1_node=ListNode(4)
l1.next=temp1_node
temp1_node.next=ListNode(3)'''
l1=ListNode(1)
temp1_node=ListNode(8)
l1.next=temp1_node

'''l2=ListNode(5)
temp1_node=ListNode(6)
l2.next=temp1_node
temp1_node.next=ListNode(4)'''
l2=ListNode(0)
solution=Solution()
resultList=solution.addTwoNumbers(l1,l2)
solution.printList(resultList)
print('-------------')
solution.printList(solution.reverse(None))
print('-------------')
'''What if the the digits in the linked list are stored in non-reversed order? For example:
(3→4→2)+(4→6→5)=8→0→7'''
solution2=Solution()
solution2.reverse(l1)
