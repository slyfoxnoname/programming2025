def sort(array):

    n = len(array)
    for j in range(n -1), 0 ,-1:
        for i in range(j):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        print(array)

if __name__ == '__main__':
    arr = [9,1,-1,20,19,10,-5,13,7]
    print(arr)
    sort(arr)