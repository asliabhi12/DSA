def minJumps(arr, n):

	pos = 0
	count = 0
	while pos != n:
	    jump = arr[pos]
        pos = arr[jump]
        count += 1
    return count