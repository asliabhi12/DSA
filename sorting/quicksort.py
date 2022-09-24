from cmath import pi


def partition(a,l, h):
    pivot = a[l]
    i = l
    j = h

    while i < j:
        while a[i] <= pivot: i+=1
        while a[j] > pivot: j-=1
        if i < j:
            a[i], a[j] = a[j], a[i]

    a[j], a[l] = a[l], a[j]

    return j

def quicksort(a, l, h):
    if l < h :
        pivot = partition(a, l, h)
        quicksort(a,l, pivot-1)
        quicksort(a,pivot+1, h)
    return a



arr = [8,4,6,2,1,9,0]
size = len(arr)
print(quicksort(arr, 0, size-1))
