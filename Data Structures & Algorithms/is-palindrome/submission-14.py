class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1

        while start<=end:
            a = s[start]
            b = s[end]

            if a.isalnum() and b.isalnum():
                if a.lower() == b.lower():
                    start += 1
                    end   -= 1
                else:
                    return False
            elif not a.isalnum():
                start += 1
            else:
                end -= 1
        return True

