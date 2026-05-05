class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(filter(lambda x: x.isalnum(), s.lower()))
        return clean_s[::-1] == clean_s
        