def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    while l < r:
        m = l + (r - l) // 2
        print(f"l:{l}, m:{m}, r:{r}, arr[m]: {arr[m]}")
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return l


if __name__ == '__main__':
    a = [0,0,1,2,2,3,3,7,7,8,10,11,11,12]
    x = 9
    i = binary_search(a, x)
    print(i)