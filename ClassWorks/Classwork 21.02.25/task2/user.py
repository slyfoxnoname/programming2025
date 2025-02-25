def sort(array):

    n = len(array)
    for i in range(1,n):
        pos = i
        x = array[pos]
        while pos > 0:
            if array[pos - 1] > x:
                array[pos] = array[pos - 1]
            else:
                break
            pos -= 1
        array[pos] = x
        print(array)


if __name__ == '__main__':
    arr = [9,1,-1,20,19,10,-5,13,7]
    # arr = [3,6,7,10,15,3]
    print(arr)
    sort(arr)