class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {}
        max_len = 0
        left = 0
        
        for right in range(len(s)):
            # If the character is a duplicate and occurs after or at 'left'
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1
            
            # Update the character's last seen index
            char_map[s[right]] = right
            
            # Update max_len if the current window is longer
            max_len = max(max_len, right - left + 1)
            
        return max_len
