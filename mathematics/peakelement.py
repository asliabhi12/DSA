from operator import indexOf


def peakElement(arr, n):
        print(arr.index(max(arr)))
        # Code here
        if max(arr) > min(arr):
            return 1
        else: return 0

print(peakElement([1,2,3], 3))