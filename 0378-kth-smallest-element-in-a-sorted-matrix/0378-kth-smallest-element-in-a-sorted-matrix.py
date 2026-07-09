class Solution(object):
    def kthSmallest(self, matrix, k):
        sort=[item for row in matrix for item in row]
        sort=sorted(sort)
        ans=sort[k-1]
        return ans
        