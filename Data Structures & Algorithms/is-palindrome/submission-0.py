class Solution:
    def isPalindrome(self, s: str) -> bool:
         word = "".join(char for char in s if char.isalnum()).strip().lower()
         return word==word[::-1]
        
        