# 13 - https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        
        hashMap = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        # scan from left to right and add
        # but pay attention to the edge case
        # if curr_num <= next_num [subtract]
        
        result = 0
        
        for idx in range(len(s)-1):
            
            if hashMap[s[idx]] >= hashMap[s[idx+1]]:
                result += hashMap[s[idx]]
            else:
                result -= hashMap[s[idx]]
                
        result += hashMap[s[-1]]
        
        return result 

