def main(arr: list)-> list:
    """
    parameters: an array
    output: array
    time complexity: linear O(nlogn) sort + O(logn) binary search + O(n) while loop = O(nlogn)
    """
    res = []
    arr.sort()
    li = [i for i in range(1, len(arr)+1)]
    while li:
        s = li.pop(0)
        # binary search with slices
        l, r = 0, len(arr)-1
        while l <= r:
            mid = (l+r)//2
            # print(f'{arr[l:r+1]=}, {s=}, {r=}, {l=}, {mid=}, {arr[mid]=}, {li=}')
            if arr[mid] == s:
                # print('found')
                break
            elif arr[mid] < s:
                l = mid + 1
            else:
                r = mid - 1
        if l == r+1:
            res.append(s)
            # print(f'{res=}')
    return res
        
        
        
    

if __name__ == "__main__":
    inputs = [[4, 3, 2, 7, 8, 2, 3, 1], [1, 1]]
    for i in inputs:
        print(main(i))