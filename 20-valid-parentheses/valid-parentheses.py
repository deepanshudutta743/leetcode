class Solution:
    def isValid(self, s: str) -> bool:
        # while '()' in s or '{}' in s or '[]' in s:
        #     s=s.replace('()','')
        #     s=s.replace('{}','')
        #     s=s.replace('[]','')
        # return s==''

        stack=[]
        closeToOpen={')':'(','}':'{',']':'['}

        for ch in s:
            if ch in closeToOpen:
                if stack and stack[-1]==closeToOpen[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        

        return True if not stack else False


        