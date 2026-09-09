class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    
        stack = []
        
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
            else:
                match token:
                    case '+':
                        result = stack.pop() + stack.pop()
                        stack.append(result)
                    case '-':
                        b, a = stack.pop(), stack.pop()
                        stack.append(a - b)
                    case '*':
                        result = stack.pop() * stack.pop()
                        stack.append(result)
                    case '/':
                        b, a = stack.pop(), stack.pop()
                        stack.append(int(a / b))
        
        return stack.pop()