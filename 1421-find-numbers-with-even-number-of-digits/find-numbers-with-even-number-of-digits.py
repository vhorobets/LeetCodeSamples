class Solution(object):
    def findNumbers(self, nums):
        def digitNumber(n):
            res = 0
            while n != 0:
                n //= 10
                res += 1
            return res

        k = 0
        for n in nums:
            if digitNumber(n) % 2 == 0:
                k += 1
        
        return k
    
        