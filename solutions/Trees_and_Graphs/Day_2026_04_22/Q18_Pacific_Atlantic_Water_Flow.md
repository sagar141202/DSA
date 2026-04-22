# Pacific Atlantic Water Flow

## Problem Statement
Given an m x n matrix of non-negative integers representing the height of each cell in a continent, the Pacific ocean touches the left and top edge of the matrix, and the Atlantic ocean touches the right and bottom edge. Water can only flow from a cell to its four neighboring cells if the neighboring cell's height is greater than or equal to the current cell's height. Find all cells that water can flow to both the Pacific and Atlantic oceans. The input matrix will be between 1 and 200 rows and 1 and 200 columns, and the values in the matrix will be between 0 and 10^5.

## Approach
We will use a depth-first search (DFS) algorithm to traverse the matrix from both the Pacific and Atlantic oceans. By maintaining separate sets of visited cells for each ocean, we can find the cells that are reachable from both oceans. The algorithm starts from the edges of the matrix and explores the neighboring cells that have a greater or equal height.

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
        
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<bool>> pacific(m, vector<bool>(n, false));
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));
        
        // DFS from Pacific ocean
        for (int i = 0; i < m; i++) {
            dfs(matrix, pacific, i, 0);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, pacific, 0, j);
        }
        
        // DFS from Atlantic ocean
        for (int i = 0; i < m; i++) {
            dfs(matrix, atlantic, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, atlantic, m - 1, j);
        }
        
        // Find common cells
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
        int m = matrix.size();
        int n = matrix[0].size();
        visited[i][j] = true;
        
        // Explore neighboring cells
        int directions[][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (int k = 0; k < 4; k++) {
            int x = i + directions[k][0];
            int y = j + directions[k][1];
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
- Use DFS to traverse the matrix from both oceans.
- Maintain separate sets of visited cells for each ocean.
- Find common cells that are reachable from both oceans.