# 371 - https://leetcode.com/problems/sum-of-two-integers/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # a will store the sum
        # b will store the carry
        
        # edge case: negative values!
        # we'll have an infinite loop for negative values
        # therefore we have to keep the integer to int32
        MASK = 0xFFFFFFFF
        
        while b:    
            curr_carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = curr_carry & MASK
            
        # calculate the two's complement of the returning number
        # if it's infinite
        
        # ~ invert the bits
        
        return ~(a^MASK) if (a >> 31) & 1 else a
            
        
            
        