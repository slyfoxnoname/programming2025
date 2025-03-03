def solve(nums: str, pieces: int, value: int):
    ...



if __name__ == '__main__':
    f = open("input.txt")
    for line in f:
        n,m = line.split()
        solve(n,int(m),)
    f.close()