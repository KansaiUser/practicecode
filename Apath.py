import heapq

grid = [
  [0, 1, 0, 0],
  [0, 1, 0, 1],
  [0, 0, 0, 0],
  [1, 1, 1, 0]
]

def heuristic(a,b):
    # Manhattan distance
    return abs(a[0]-b[0])+ abs(a[1] -b[1])

def a_star(grid):
    n,m = len(grid), len(grid[0])
    start,goal = (0, 0), (n - 1, m - 1)
    print(start, goal)
    # goal = (0,0)   
    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return []

    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start,goal),0,start,[start]))

    visited = set()
    print(f"Openset {open_set}")

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = current[0]+dx, current[1]+dy
            neighbor =(nx,ny)
            if 0 <= nx < n and 0 <= ny < m and  grid[nx][ny] == 0 and  neighbor not in visited:
                new_g = g + 1
                f_score = new_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, new_g, neighbor, path+ [neighbor] ))
    return []




print(f"ruta {a_star(grid)}")
