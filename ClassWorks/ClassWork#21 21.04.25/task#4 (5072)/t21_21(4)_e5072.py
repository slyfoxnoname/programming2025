def main():
    n = int(input())
    count = 0
    for _ in range(n):
        row = list(map(int, input().split()))
        count += sum(row)
    print(count)
main()