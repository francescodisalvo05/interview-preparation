# 14 - 

# space = O(1) | time = O(N)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        length = len(strs[0]) # anyone is ok, since they should have the same pref
        
        prefix = ""
        
        for idx in range(length):
            curr_char = strs[0][idx]
            for s in strs[1:]:
                if s[idx] != curr_char:
                    return prefix
            prefix += curr_char
            
        return prefix

# space = O(1) | time = O(nlogn)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort()
        prefix = ""
        
        # they will be ordered in terms of length
        # 1st : shorter
        # last : longer
        
        # therefore compare first and last
        for idx in range(len(strs[0])):
            if strs[-1][idx] == strs[0][idx]:
                prefix += strs[0][idx]
            else: break # handle [""] and ["",""] cases

        return prefix

