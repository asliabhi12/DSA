def reverse(S):
    arr = []
    for c in S:
        arr.append(c)
    str = ""
    for i in range(len(arr)):
        str += arr.pop()

    return str

s = "Hello"
print(reverse(s))