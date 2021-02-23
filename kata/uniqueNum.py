# Solution by PauloBA

def find_uniq(arr):
    arr.sort()
    if arr[0] == arr[1]:
        ans = arr[-1]
    else:
        ans = arr[0]
    return ans