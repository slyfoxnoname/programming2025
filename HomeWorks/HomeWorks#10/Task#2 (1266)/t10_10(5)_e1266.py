def find_max_recording(n, tracks):
    max_sum = 0

    def backtrack(index, current_sum):
        nonlocal max_sum
        if current_sum > n or index == len(tracks):
            return
        max_sum = max(max_sum, current_sum)
        for i in range(index + 1, len(tracks)):
            if current_sum + tracks[i] <= n:
                backtrack(i, current_sum + tracks[i])

    backtrack(-1, 0)
    return max_sum


while True:
    try:
        line = input()
        if not line:
            break
        data = list(map(int, line.split()))
        n, s, tracks = data[0], data[1], data[2:]
        print("sum:" + str(find_max_recording(n, tracks)))
    except EOFError:
        break