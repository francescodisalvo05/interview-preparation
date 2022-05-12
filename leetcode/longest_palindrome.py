# 409 - https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        # each letter should have an even frequency
        # except for one (for odd sequences)
        
        output = 0
        hashMap = defaultdict(int)
        
        for c in s:
            hashMap[c] += 1
            
        for counter in hashMap.values():
            
            # take the "even" part
            output += counter // 2 * 2
            
            # if output is even (therefore we have space for 1 digit),
            # and counter is odd, add it
            if output % 2 == 0 and counter  % 2 == 1:
                output += 1
                
            # in practise we are taking all the "even" part of
            # every digit and then we take only one randomly 
            # from an odd frequency
            
        return output
            
            
            
            
            
        