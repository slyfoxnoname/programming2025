from collections import deque

def find_positions(grid, n):
    start = end = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '@':
                start = (i, j)
            elif grid[i][j] == 'X':
                end = (i, j)
    return start, end

def bfs(grid, start, end, n):
    visited = [[False]*n for _ in range(n)]
    prev = [[None]*n for _ in range(n)]
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while q:
        x, y = q.popleft()
        if (x, y) == end:
            break
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] in ('.', 'X') and not visited[nx][ny]:
                    visited[nx][ny] = True
                    prev[nx][ny] = (x, y)
                    q.append((nx, ny))

    if not visited[end[0]][end[1]]:
        return None

    path = []
    x, y = end
    while (x, y) != start:
        path.append((x, y))
        x, y = prev[x][y]
    path.reverse()
    return path

def mark_path(grid, path, start, end):
    for x, y in path:
        if (x, y) != end:
            grid[x][y] = '+'
    ex, ey = end
    grid[ex][ey] = '+'
    return grid

if __name__ == '__main__':
    with open("input.txt") as f:
        n = int(f.readline())
        grid = [list(f.readline().strip()) for _ in range(n)]

    start, end = find_positions(grid, n)
    path = bfs(grid, start, end, n)

    if path is None:
        print("N")
    else:
        print("Y")
        grid = mark_path(grid, path, start, end)
        for row in grid:
            print(''.join(row))
