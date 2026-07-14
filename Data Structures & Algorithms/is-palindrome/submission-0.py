class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        s = s.lower()
        for i in s:
            if i.isalnum():
                newS += i
        
        return newS == newS[::-1]

        