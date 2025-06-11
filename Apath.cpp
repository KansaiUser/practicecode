#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <tuple>
#include <algorithm>

using namespace std;

struct Node {
    int f;    // total cost = g + h
    int g;    // cost so far
    int x, y;
    vector<pair<int,int>> path;

    // For priority queue: smallest f on top
    bool operator<(const Node& other) const {
        return f > other.f; // reversed because priority_queue is max-heap by default
    }
};

// Manhattan distance heuristic
int heuristic(int x, int y, int gx, int gy) {
    return abs(gx - x) + abs(gy - y);
}

vector<pair<int,int>> a_star(const vector<vector<int>>& grid) {
    int n = grid.size();
    int m = grid[0].size();
    pair<int,int> start = {0, 0};
    pair<int,int> goal = {n-1, m-1};

    if (grid[start.first][start.second] == 1 || grid[goal.first][goal.second] == 1)
        return {};

    priority_queue<Node> open_set;
    set<pair<int,int>> visited;

    open_set.push({heuristic(0, 0, goal.first, goal.second), 0, 0, 0, {{0,0}}});

    while (!open_set.empty()) {
        Node current = open_set.top();
        open_set.pop();

        if (visited.count({current.x, current.y})) continue;
        visited.insert({current.x, current.y});

        if (current.x == goal.first && current.y == goal.second)
            return current.path;

        // Explore neighbors
        vector<pair<int,int>> directions = {{-1,0}, {1,0}, {0,-1}, {0,1}};
        for (auto [dx, dy] : directions) {
            int nx = current.x + dx;
            int ny = current.y + dy;

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (grid[nx][ny] == 1) continue;
            if (visited.count({nx, ny})) continue;

            int new_g = current.g + 1;
            int new_f = new_g + heuristic(nx, ny, goal.first, goal.second);
            vector<pair<int,int>> new_path = current.path;
            new_path.push_back({nx, ny});

            open_set.push({new_f, new_g, nx, ny, new_path});
        }
    }

    return {}; // No path found
}

int main() {
    vector<vector<int>> grid = {
        {0, 1, 0, 0},
        {0, 1, 0, 1},
        {0, 0, 0, 0},
        {1, 1, 1, 0}
    };

    vector<pair<int,int>> path = a_star(grid);

    if (path.empty()) {
        cout << "No route was found." << endl;
    } else {
        cout << "Path found:" << endl;
        for (auto [x,y] : path) {
            cout << "(" << x << "," << y << ") ";
        }
        cout << endl;
    }

    return 0;
}
