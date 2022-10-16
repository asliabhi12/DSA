def rotate(s ,d):
    lFirst = s[0 : d]

    lLast = s[d :]

    rFirst = s[0 : len(s) -d]
    rLast = s[len(s) - d: ]

    print(f"left rotate by {d} is {lLast + lFirst}")
    print(f"right rotate by {d} is {rLast + rFirst}")


s = "GeeksforGeeks"

rotate(s, 2)