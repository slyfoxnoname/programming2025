def dfs_mark(x, y, label):
    stack = [(x, y)]
    area = 0
    while stack:
        cx, cy = stack.pop()
        if not (0 <= cx < H and 0 <= cy < W):
            continue
        if visited[cx][cy] != 0 or grid[cx][cy] != '*':
            continue
        visited[cx][cy] = label
        area += 1
        stack.extend([(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)])
    return area

def dfs_hole(x, y, mask):
    stack = [(x, y)]
    seen = []
    is_hole = True
    while stack:
        cx, cy = stack.pop()
        if not (0 <= cx < H and 0 <= cy < W):
            continue
        if mask[cx][cy] or grid[cx][cy] != '.':
            continue
        mask[cx][cy] = True
        seen.append((cx, cy))
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < H and 0 <= ny < W):
                is_hole = False  # межа поля
            elif grid[nx][ny] == '.' and not mask[nx][ny]:
                stack.append((nx, ny))
    return is_hole, seen


with open("input.txt") as f:
    W, H = map(int, f.readline().split())
    grid = [list(f.readline().strip()) for _ in range(H)]

    visited = [[0] * W for _ in range(H)]
    label = 1
    components = {}

    for i in range(H):
        for j in range(W):
            if grid[i][j] == '*' and visited[i][j] == 0:
                area = dfs_mark(i, j, label)
                components[label] = {'area': area, 'holes': 0}
                label += 1

    mask = [[False]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.' and not mask[i][j]:
                is_hole, seen = dfs_hole(i, j, mask)
                if not is_hole:
                    continue
                border_labels = set()
                for x, y in seen:
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < H and 0 <= ny < W:
                            if grid[nx][ny] == '*':
                                border_labels.add(visited[nx][ny])
                if len(border_labels) == 1:
                    label_id = border_labels.pop()
                    components[label_id]['holes'] += 1

    max_holes = -1
    min_area = 0
    for data in components.values():
        if data['holes'] > max_holes:
            max_holes = data['holes']
            min_area = data['area']
        elif data['holes'] == max_holes:
            min_area = min(min_area, data['area'])

    print(min_area if max_holes > 0 else 0)
