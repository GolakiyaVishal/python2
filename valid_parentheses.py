""" 
Given a string s containing just character '{','}','(',')','[' and ']'
determind the input string is valid
An input string is valid if
 	1. Open bracket must be closed by the same type of brackets.
 	2. Open bracket must be closed in the correct order.

"""

def solution(s):
    stack = []
    for e in list(s):
        if e == ")" or e == "}" or e == "]":
            if len(stack) == 0:
                return False
            tp = stack.pop()
            if (e == ")" and tp != "(") or (e == "}" and tp != "{") or (e == "]" and tp != "["):
                return False
        else:
            stack.append(e)
    
    return len(stack) == 0
    

if __name__ == '__main__':
        result = solution("({[]})")
        print(result)