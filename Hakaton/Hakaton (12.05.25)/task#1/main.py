from collections import deque
def bfs(start_x, start_y, maze, N, M):
    dist = [[-1] * M for _ in range(N)]
    queue = deque()
    queue.append((start_x, start_y))
    dist[start_x][start_y] = 0

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    return dist

if __name__ == '__main__':
    with open("input.txt") as f:
        N, M = map(int, f.readline().split())
        p_x, p_y = map(int, f.readline().split())
        v_x, v_y = map(int, f.readline().split())

        # координати з 1-based до 0-based
        p_x -= 1
        p_y -= 1
        v_x -= 1
        v_y -= 1

        maze = [list(map(int, f.readline().split())) for _ in range(N)]

        dist_petya = bfs(p_x, p_y, maze, N, M)
        dist_vasya = bfs(v_x, v_y, maze, N, M)

        min_time = float('inf')
        meet_point = (-1, -1)

        for i in range(N):
            for j in range(M):
                if dist_petya[i][j] != -1 and dist_vasya[i][j] != -1:
                    time = max(dist_petya[i][j], dist_vasya[i][j])
                    if time < min_time:
                        min_time = time
                        meet_point = (i + 1, j + 1)  # повертаємо до 1-based

        if meet_point == (-1, -1):
            print(-1)
        else:
            print(*meet_point)
