# 278 - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# space = O(1) | time = O(logn)
class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        L, R = 1, n
        
        while L <= R:
            # shift ahead by (R - L) // 2
            M = L + (R - L) // 2
            
            # check if it's bad
            if isBadVersion(M):
                # if the previous it's not bad,
                # it is the broken one
                if not isBadVersion(M - 1):
                    return M
                # otherwise it will be before
                else:
                    R = M - 1
            # otherwise it will be ahead
            else:
                L = M + 1
            
        return -1
        