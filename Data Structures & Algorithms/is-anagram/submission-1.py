class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time: O(nlogn + mlogm)
        # Space: O(1) or depending on the sorting algorithm O(N)
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
        