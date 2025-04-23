def main():
    n = int(input())
    count = 0
    for _ in range(n):
        row = list(map(int, input().split()))
        if sum(row) == 1:
            count += 1
    print(count)

main()
