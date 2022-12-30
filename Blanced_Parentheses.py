def are_pair(open,close):
    if open == '(' and close ==')':
        return True
    elif open == '{' and close == '}':
        return True
    elif open == '[' and close == ']':
        return True

    return False

def areBalanced(exp):
    stack = []
    for ch in exp :
        if ch == '(' or ch =='{' or ch == '[':
            stack.append(ch)

        elif ch == ')' or ch =='}' or ch == ']':
            if len(stack) == 0 or not are_pair(stack[-1], ch):
                return False
            else :
                stack.pop()
    return len(stack) == 0


expression  = input("Enter an expression : ")    
if areBalanced(expression):
    print('Balanced')   
else : 
    print("Are not Balanced")