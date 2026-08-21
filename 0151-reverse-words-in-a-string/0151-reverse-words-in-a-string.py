class Solution(object):
    def reverseWords(self, s):
        lst = s.split()
        l, r = 0, len(lst) - 1 
        
        while l < r:
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1
            
        return " ".join(lst)