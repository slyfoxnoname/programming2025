def sort(array):
    n = len(array)
    for num_pass in range(n - 1, 0 ,-1):
        for i in range(num_pass):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        print(array)

if __name__ == '__main__':
    array = [8, 3, 7, 1, 5, 6, 2, 4,7 ,9 ,0]
    print(sort(array))
