class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean = "".join(char for char in s if char.isalnum())
        clean = clean.lower()

        for i in range(len(clean)//2):
            if clean[i] != clean[-1-i]:
                print(clean[i], clean[-1-i])
                return False
        return True