# Pacific Atlantic Water Flow

## Problem Statement
There is a rectangular matrix of m x n cells, representing a piece of land where each cell can hold a certain amount of water. Each cell has an elevation, and water can flow from a cell to its adjacent cells (up, down, left, right) if the elevation of the adjacent cell is lower or equal. There are two oceans: the Pacific Ocean and the Atlantic Ocean. The Pacific Ocean is on the left and top sides of the matrix, while the Atlantic Ocean is on the right and bottom sides. We need to find all the cells from which water can flow to both oceans.

## Approach
We can use a Depth-First Search (DFS) algorithm to traverse the matrix from the Pacific and Atlantic Oceans. By maintaining two separate sets of visited cells for each ocean, we can identify the cells that are reachable from both oceans.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

void dfs(vector<vector<int>>& matrix, vector<vector<bool>>& visited, int i, int j, int m, int n) {
    visited[i][j] = true;
    vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    for (auto& dir : directions) {
        int x = i + dir.first;
        int y = j + dir.second;
        if (x >= 0 && x < m && y >= 0 && y < n && !visited[x][y] && matrix[x][y] >= matrix[i][j]) {
            dfs(matrix, visited, x, y, m, n);
        }
    }
}

vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
    if (matrix.empty() || matrix[0].empty()) return {};
    int m = matrix.size();
    int n = matrix[0].size();
    vector<vector<bool>> pacific(m, vector<bool>(n, false));
    vector<vector<bool>> atlantic(m, vector<bool>(n, false));
    
    // dfs from pacific
    for (int i = 0; i < m; i++) {
        dfs(matrix, pacific, i, 0, m, n);
    }
    for (int j = 0; j < n; j++) {
        dfs(matrix, pacific, 0, j, m, n);
    }
    
    // dfs from atlantic
    for (int i = 0; i < m; i++) {
        dfs(matrix, atlantic, i, n - 1, m, n);
    }
    for (int j = 0; j < n; j++) {
        dfs(matrix, atlantic, m - 1, j, m, n);
    }
    
    vector<vector<int>> result;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (pacific[i][j] && atlantic[i][j]) {
                result.push_back({i, j});
            }
        }
    }
    return result;
}
```

## Test Cases
```
Input: 
[
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]
Output: 
[
  [0,4],
  [1,3],
  [1,4],
  [2,2],
  [3,0],
  [3,1],
  [4,0]
]
```

## Key Takeaways
- Use DFS to traverse the matrix from both oceans.
- Maintain two separate sets of visited cells for each ocean.
- Identify the cells that are reachable from both oceans by checking the intersection of the two visited sets.