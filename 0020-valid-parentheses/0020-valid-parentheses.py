class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s :
            if i == '(' :
                stack.append(i)
            
            elif i == '{' :
                stack.append(i)
            
            elif i == '[' :
                stack.append(i)
        
            elif i == ')' :
                if len(stack) == 0 or stack.pop() != '(' :
                    return False
            
            elif i == '}' :
                if len(stack) == 0 or stack.pop() != '{' :
                    return False
            
            elif i == ']' :
                if len(stack) == 0 or stack.pop() != '[' :
                    return False
    
        if len(stack) == 0 :
            return True
        else : 
            return False