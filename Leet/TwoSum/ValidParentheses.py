##AlexSteeves



class Solution(object):
        def isValid(self, s):
                """
                :type s: str
                :rtype: bool
                """

                stack = []

                for char in s:
                    if char in ['(', '{', '[']:
                        stack.append(char)
                    elif len(stack)!=0 and stack[-1]=='(' and char == ')':
                          stack.pop()
                    elif len(stack)!=0 and stack[-1]=='{' and char == '}':
                          stack.pop()
                    elif len(stack)!=0 and stack[-1]=='[' and char == ']':
                          stack.pop()
                    else:
                        return False
                return stack == []
                    
                              
                              
                                         