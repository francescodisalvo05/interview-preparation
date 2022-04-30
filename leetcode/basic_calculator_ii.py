# 227 - https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        
        stack, curr_num, operator = [], 0, "+"
    
        # fake the final "sum"
        for char in s + "+":
            
            if char.isnumeric():
                
                # edge case: number with two or more digits
                curr_num = curr_num * 10 + int(char)
                
            # edge case: there can be spaces on the string e.g. ' 3/2 '
            if char in ['+','-','/','*']:
                
                if operator == '+':
                    stack.append(curr_num)
                elif operator == '-':
                    stack.append(-curr_num)
                elif operator == '*':
                    stack.append(stack.pop() * curr_num)
                elif operator == '/':
                    stack.append(int(stack.pop() / curr_num))
                    
                # reset num and update operator
                curr_num = 0
                operator = char
            
        
        return sum(stack)
            
                