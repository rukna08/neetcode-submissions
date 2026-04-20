class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        ss = ""

        # iterate through the string character by character
        for c in s:    
            # check if it's 0 - 9
            if ord(c) >= 48 and ord(c) <= 57:
                ss += c
            # check if it's a - z
            if ord(c) >= 97 and ord(c) <= 122:
                ss += c
            # check if it's A - Z
            if ord(c) >= 65 and ord(c) <= 90:
                # convert to lowercase by adding 32
                ss += chr(ord(c) + 32)
        
        
        left = 0
        right = len(ss) - 1

        while left <= right:
            if ss[left] != ss[right]:
                return False
            
            left += 1
            right -= 1

        return True