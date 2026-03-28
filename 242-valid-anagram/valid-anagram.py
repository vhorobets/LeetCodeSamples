class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        s_arr = sorted(s)
        t_arr = sorted(t)

        return all(s_arr[i] == t_arr[i] for i in range(len(s)))

        
        