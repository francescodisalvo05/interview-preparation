# 383 - https://leetcode.com/problems/ransom-note/

# space = O(1) | time = O(n*m) 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        for c in ransomNote:
            if c in magazine:
                # edge case: replace only '1' letter
                magazine = magazine.replace(c,'',1)
            else:
                return False
            
        return True


# space = O(m) | time = O(n+m)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        hashMap = defaultdict(int)
        
        for c in ransomNote:
            hashMap[c] += 1
            
        for c in magazine:
            hashMap[c] -= 1
            
        if max(hashMap.values()) <= 0:
            return True
        else:
            return False