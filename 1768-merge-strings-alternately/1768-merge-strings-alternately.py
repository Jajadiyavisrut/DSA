class Solution(object):
    def mergeAlternately(self, word1, word2):
        a=len(word1)
        b=len(word2)
        new=""
        while a>0 and b>0:
            new+=word1[len(word1)-a]
            new+=word2[len(word2)-b]
            a,b=a-1,b-1
        while a>0:
            new+=word1[len(word1)-a]
            a-=1
        while b>0:
            new+=word2[len(word2)-b]
            b-=1
        return new

