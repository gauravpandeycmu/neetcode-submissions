class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1

        while start<end:
            a = s[start]
            b = s[end]

            if not a.isalnum():
                start += 1
                continue
            if not b.isalnum():
                end -= 1
                continue
            
            if a.lower() != b.lower():
                return False
            start+=1
            end -=1
        return True

