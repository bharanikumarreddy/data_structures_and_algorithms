


class Solution:
    def MissingNumber(self,array,n):
       
        correct = n*(n+1) // 2
        wrong = sum(array)
        return correct - wrong
      
        
        
        



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
