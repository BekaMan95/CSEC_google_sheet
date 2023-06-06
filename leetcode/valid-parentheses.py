class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack) > 0 and i > 0:
                    if stack.__getitem__(len(stack)-1) == '(':
                        stack.pop()
                    else:
                        stack.append('flag')
                        break
                else:
                    stack.append('flag')
                    break
            elif s[i] == '}':
                if len(stack) > 0 and i > 0:
                    if stack.__getitem__(len(stack)-1) == '{':
                        stack.pop()
                    else:
                        stack.append('flag')
                        break
                else:
                    stack.append('flag')
                    break
            elif s[i] == ']':
                if len(stack) > 0 and i > 0:
                    if stack.__getitem__(len(stack)-1) == '[':
                        stack.pop()
                    else:
                        stack.append('flag')
                        break
                else:
                    stack.append('flag')
                    break

        if len(stack) == 0:
            return True
        else:
            return False
