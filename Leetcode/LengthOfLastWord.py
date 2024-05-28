
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words= s.split()
        print(f"last word is: {words[-1]}")
        return len(words[-1])

print(Solution().lengthOfLastWord("   Hello     gfjh            world       "))