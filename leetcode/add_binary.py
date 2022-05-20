# 67 - https://leetcode.com/problems/add-binary/

# Nice solution without "+" : https://leetcode.com/problems/add-binary/discuss/1987803/Python-bit-manipulation-solution-with-print-statements-to-use-for-understanding


# time = O(n) | space = O(1)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        x, y, carry, result = int(a,2), int(b,2), 0, 0
        
        # y will be updated with the carry
        while y:
            
            # XOR : 1 + 1 = 0
            result = x ^ y
            
            # get carry and shift
            carry = (x & y) << 1
            
            # x will have the cumulative sum and 
            # y will keep track the carry
            x, y = result, carry
            
        return bin(x)[2:] # remove 0b
            