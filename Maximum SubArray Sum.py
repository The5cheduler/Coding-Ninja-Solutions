from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :
    if not arr:
        return 0

    prev_max, max_so_far, prev_min = arr[0], arr[0], arr[0]
    for i in range(1,len(arr)):
        curr_max = max(prev_min + arr[i], prev_max + arr[i], arr[i])
        curr_min = min(prev_min + arr[i], prev_max + arr[i], arr[i])
        max_so_far = max(max_so_far,curr_max)
        prev_max = curr_max
        prev_min = curr_min
         
    return max_so_far if max_so_far > 0 else 0





#taking inpit using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
