def main():
    n = int(input())
    degrees = []
    for _ in range(n):
        row = list(map(int, input().split()))
        degrees.append(sum(row))
    print(*degrees)

main()
