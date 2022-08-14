# from queue import LifoQueue


# def isPalindrome(str):
#     stack = LifoQueue()

#     # def isOpening(c):
#     #     return '(' or '{' or '[' 

#     char = ['(', "{", "["]

#     def isMatching(a, b):
#         return a == '(' and ')' or  '{' and '}' or '[' and ']' 

#     for i in range(len(str)):
#         cur = str[i]
#         if (cur in char):
#             print("it was opening", cur)
#             stack.put(cur)
#         elif stack.empty():
#             return False
#         elif not isMatching(stack.get(), cur):
#             return False

#         else: stack.get()

#     print(stack.get())

#     return stack.empty()



# print(isPalindrome('{{}}'))


"""
In the upcoming future above technique will work

"""

def areBracketsBalanced(expr):
    stack = []
 
    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "["]:
 
            # Push the element in the stack
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    # Check Empty Stack
    if stack:
        return False
    return True