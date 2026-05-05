class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean_s = "".join(filter(lambda x: x.isalnum(), s.lower()))
        # return clean_s[::-1] == clean_s
        return "".join(filter(str.isalnum, s.lower())) == "".join(filter(str.isalnum, s.lower()))[::-1]