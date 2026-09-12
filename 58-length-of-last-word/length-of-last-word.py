class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        words=s.strip().split()
        for i in words[-1]:
            count+=1
        return count
        