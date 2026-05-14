class Solution:
    def isPalindrome(self, s: str) -> bool:

        empty = ""

        for i in s:
            if i.isalnum():
                empty += i
                
        lower = empty.lower()

        flipped = ""
        for j in range(len(lower) -1, -1, -1):
            flipped += lower[j]

        return flipped == lower