#  844 - https://leetcode.com/problems/backspace-string-compare/


# space = O(n+m) | time = O(n+m)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def get_clean_word(s):
            stack = []
            
            for c in s:
                if c == "#" and stack:
                    stack.pop()
                elif c != "#":
                    stack.append(c)
                    
            return ''.join(stack)
                    
        return get_clean_word(s) == get_clean_word(t)