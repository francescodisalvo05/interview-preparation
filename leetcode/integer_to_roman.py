# 12 - https://leetcode.com/problems/integer-to-roman/


class Solution:
    def intToRoman(self, num: int) -> str:
        
        # romanMap = corrispondence among roman and integer
        hashMap = {  
            1000 : "M",
            900  : "CM",
            500  : "D",
            400  : "CD",
            100  : "C",
            90   : "XC",
            50   : "L",
            40   : "XL",
            10   : "X",
            9    : "IX",
            5    : "V",
            4    : "IV",
            1    : "I"
        }

        roman = ''
        
        # the order is the key!
        for curr_integer, curr_roman  in hashMap.items():

            roman += (num // curr_integer) * curr_roman
            num %= curr_integer

        return roman