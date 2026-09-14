
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=""
        for x in reversed(s.lower()):
            if x.isalnum():
                new=new+x
        if new==new[::-1]:
            return True
        else:
            return False