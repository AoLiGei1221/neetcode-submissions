class Solution:
    def isPalindrome(self, s: str) -> bool:
        return "".join(filter(lambda x: x.isalnum(), s.lower())) == "".join(filter(lambda x: x.isalnum(), s.lower()))[::-1]
        