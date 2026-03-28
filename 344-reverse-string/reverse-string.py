class Solution(object):
    def reverseString(self, s):
        l = 0
        r = len(s) - 1

        while l < r:
            c = s[l]
            s[l] = s[r]
            s[r] = c
            l += 1
            r -= 1
        


        