class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        return len(list(s.split())[-1])