from collections import deque


class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.n = len(grid)
        self.m = len(grid[0]) if self.n > 0 else 0

    def is_valid(self, x, y):
        return self.n > x >= 0 == self.grid[x][y] and 0 <= y < self.m


class ShortestPathFinder:
    def __init__(self, grid):
        self.grid = grid
        self.visited = [[False for _ in range(grid.m)] for _ in range(grid.n)]
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    def bfs(self, start):
        queue = deque([(start[0], start[1], 0)])  # (x, y, distance)
        self.visited[start[0]][start[1]] = True

        while queue:
            x, y, dist = queue.popleft()

            if x == self.grid.n - 1 and y == self.grid.m - 1:
                return dist

            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy

                if self.grid.is_valid(nx, ny) and not self.visited[nx][ny]:
                    self.visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

        return -1  # No path found

    def find_shortest_path(self):
        if self.grid.n == 0 or self.grid.m == 0 or not self.grid.is_valid(0, 0):
            return -1

        return self.bfs((0, 0))


# Usage
grid_data = [
    [0, 0, 0, 1],
    [1, 0, 1, 0],
    [0, 0, 0, 0]
]
grid = Grid(grid_data)
path_finder = ShortestPathFinder(grid)
shortest_path_length = path_finder.find_shortest_path()
print(f"The shortest path is {shortest_path_length} steps.")
