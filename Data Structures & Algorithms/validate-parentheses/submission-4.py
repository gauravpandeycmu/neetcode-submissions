class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        def check(top, c):
            if top=="(" and c==")":
                return True
            elif top=="[" and c=="]":
                return True
            elif top=="{" and c=="}":
                return True
            else:
                return False
            

        for c in s:

            if c=="(" or c=="[" or c=="{":
                stack.append(c)
            elif c==")" or c=="]" or c=="}":
                if len(stack)>0 and check(stack[-1], c):
                    stack.pop()
                else:
                    return False

        return len(stack)==0