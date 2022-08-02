def search2dmat(matrix, target):
    def binarySearch(arr, target):
        low = 0
        high = len(arr) - 1
        mid = low + high // 2

        while low < high:
            if target < arr[mid]:
                high = mid - 1

            if target == arr[mid]:
                return True
               

            else:
                low = mid + 1

            mid = (high + low) // 2

        return True if arr[mid] == target else False

    for i in range(len(matrix)):

        if target <= matrix[i][-1]:
            return binarySearch(matrix[i], target)

        return False

mat = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

tar = 4

print(search2dmat(mat, tar))

        












