# 49 - https://leetcode.com/problems/group-anagrams/


# space = O(n) | time = O(nlogn)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # property of an anagrams
        # - if we order the words, they will be equal
        
        hashMap = defaultdict(list)
        
        for s in strs:
            hashMap[''.join(sorted(s))].append(s)
            
        return hashMap.values()
        
        