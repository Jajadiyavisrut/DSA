class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        empty_plots = 1 
        
        for num in flowerbed:
            if num == 0:
                empty_plots += 1
                if empty_plots == 3:
                    n -= 1
                    empty_plots = 1
            else:
                empty_plots = 0
                
        if empty_plots == 2:
            n -= 1
            
        return n <= 0
