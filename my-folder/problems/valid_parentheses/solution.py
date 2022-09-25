class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) > 0:
                    p = stack.pop()
                    if c == ')' and p != '(':
                        return False
                    elif c == '}' and p != '{':
                        return False
                    elif c == ']' and p != '[':
                        return False
                    else:
                        continue
                else:
                    return False
        if len(stack) > 0:
            return False
        return True
#         matches = {
#             "}":"{", "]":"[", ")":"("
#         } 
        
#         stack = []
        
#         for char in s:
            
#             if char not in matches:
#                 stack.append(char)
                
#             else:
#                 if not stack or stack.pop() != matches[char]:
#                     return False
                
#         return len(stack) == 0
        