# Pacific Atlantic Water Flow

## Problem Statement
There is a 2D grid of size m x n, where each cell can hold a certain amount of water. The Pacific Ocean is located to the left and top of the grid, and the Atlantic Ocean is located to the right and bottom. Water can flow from a cell to its neighboring cells if the neighboring cell has a higher or equal height. Find all the cells from which water can flow to both the Pacific and Atlantic Oceans.

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the grid from both the Pacific and Atlantic Oceans. It maintains two separate sets of visited cells for each ocean and returns the intersection of these sets.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return {};
        
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<bool>> pacific(m, vector<bool>(n, false));
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));
        
        // DFS from Pacific Ocean
        for (int i = 0; i < m; i++) {
            dfs(matrix, pacific, i, 0);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, pacific, 0, j);
        }
        
        // DFS from Atlantic Ocean
        for (int i = 0; i < m; i++) {
            dfs(matrix, atlantic, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
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
        if (visited[i][j]) return;
        visited[i][j] = true;
        
        int m = matrix.size(), n = matrix[0].size();
        int directions[][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        for (int k = 0; k < 4; k++) {
            int x = i + directions[k][0], y = j + directions[k][1];
            if (x >= 0 && x < m && y >= 0 && y < n && matrix[x][y] >= matrix[i][j]) {
                dfs(matrix, visited, x, y);
            }
        }
    }
};

```

## Test Cases
```
Input: [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

## Key Takeaways
- Use DFS to traverse the grid from both oceans.
- Maintain separate sets of visited cells for each ocean.
- Return the intersection of the two sets of visited cells.