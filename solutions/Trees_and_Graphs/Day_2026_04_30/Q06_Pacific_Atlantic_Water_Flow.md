# Pacific Atlantic Water Flow

## Problem Statement
There is a matrix of size m x n, representing a map with some obstacles. Water can flow from any cell to its adjacent cells (up, down, left, right) if the adjacent cell has a higher or equal height. There are two oceans, the Pacific Ocean and the Atlantic Ocean, which are located at the left and right edges, and the top and bottom edges of the map respectively. We need to find all the cells from which water can flow to both the Pacific and Atlantic Oceans.

## Approach
The approach is to use Depth-First Search (DFS) to traverse the grid from both the Pacific and Atlantic Oceans. We will start from the edges of the grid and mark all the cells that can be reached by water from each ocean. Then, we will find the intersection of the two sets of cells to get the cells from which water can flow to both oceans.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return {};
        
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<bool>> pacific(m, vector<bool>(n, false));
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));
        
        for (int i = 0; i < m; i++) {
            dfs(matrix, pacific, i, 0);
            dfs(matrix, atlantic, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, pacific, 0, j);
            dfs(matrix, atlantic, m - 1, j);
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
    
    void dfs(vector<vector<int>>& matrix, vector<vector<bool>>& visited, int i, int j) {
        visited[i][j] = true;
        int m = matrix.size(), n = matrix[0].size();
        vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        for (auto& dir : directions) {
            int x = i + dir.first, y = j + dir.second;
            if (x >= 0 && x < m && y >= 0 && y < n && !visited[x][y] && matrix[x][y] >= matrix[i][j]) {
                dfs(matrix, visited, x, y);
            }
        }
    }
};
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
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

## Key Takeaways
- Use DFS to traverse the grid from the edges of the Pacific and Atlantic Oceans.
- Mark all the cells that can be reached by water from each ocean using separate boolean matrices.
- Find the intersection of the two sets of cells to get the cells from which water can flow to both oceans.