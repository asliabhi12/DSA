def leaders(A, N):
        curlargest = A[N-1]
        leader = [A[N-1]]
        for i in range(N-2, -1, -1):
            if A[i] >= curlargest:
                leader.append(A[i])
                curlargest = A[i]

        return leader[::-1]

arr = [16,17,4,3,5,2]

print(leaders(arr, len(arr)))
