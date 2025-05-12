import sys

sys.setrecursionlimit(10000)


def dfs(grid, x, y, m, n, visited):
    visited[x][y] = True
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n:
            if grid[nx][ny] == '#' and not visited[nx][ny]:
                dfs(grid, nx, ny, m, n, visited)


if __name__ == '__main__':
    with open("input.txt") as f:
        m, n = map(int, f.readline().split())
        grid = [list(f.readline().strip()) for _ in range(m)]

    visited = [[False] * n for _ in range(m)]
    components = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '#' and not visited[i][j]:
                dfs(grid, i, j, m, n, visited)
                components += 1

    print(components)
