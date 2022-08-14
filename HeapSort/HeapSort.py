
def swap(lst, i, j):
    lst[i] ,lst[j] = lst[j], lst[i]

def siftDown(lst, i, upper):
    while True:
        l,r = i*2+1, i*2+2
        # check if there are two childs are greater than upper element
        if max(l, r) < upper:
            if lst[i] >= max(lst[l],lst[r]): break
            elif lst[l] > lst[r]:
                swap(lst, i, l)
                i = l
            else: 
                swap(lst, i, r)
                i = r
        elif l < upper:
            if lst[l] > lst[i]:
                swap(lst, i, l)
                i = l
            else:
                break
        elif r < upper:
            if lst[r] > lst[i]:
                swap(lst, i, r)
        else:
            break
    

def heapSort(nums):
    for j in range(len(nums)//2, -1, -1):
        siftDown(nums, j, len(nums))

    for end in range(len(nums)-1, 0, -1):
        swap(nums, 0, end)
        siftDown(nums, 0, end)

lst = [5,16,8,14,20,1,26]
heapSort(lst)
print(lst)