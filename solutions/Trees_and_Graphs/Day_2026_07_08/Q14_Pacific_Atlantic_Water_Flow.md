# Pacific Atlantic Water Flow

## Problem Statement
Given an m x n matrix of non-negative integers representing the height of each cell in a grid, find the cells from which water can flow to both the Pacific and Atlantic oceans. Water can flow from a cell to another cell if the height of the former cell is greater than or equal to the height of the latter cell. The Pacific ocean is on the left and top sides of the grid, while the Atlantic ocean is on the right and bottom sides. Return a vector of vectors, where each inner vector contains two integers representing the row and column of a cell from which water can flow to both oceans. The input grid will have at least one cell, and the number of cells will not exceed 5 * 10^5. The height of each cell will be in the range [0, 10^5].

## Approach
We can use a depth-first search (DFS) algorithm to traverse the grid and find the cells from which water can flow to both oceans. We will start the DFS from the Pacific and Atlantic ocean borders and mark the reachable cells. Then, we will find the cells that are reachable from both oceans.

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
        
        // Pacific DFS
        for (int i = 0; i < m; i++) {
            dfs(matrix, pacific, i, 0);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, pacific, 0, j);
        }
        
        // Atlantic DFS
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
        if (visited[i][j]) return;
        visited[i][j] = true;
        
        int m = matrix.size(), n = matrix[0].size();
        int directions[][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (int k = 0; k < 4; k++) {
            int ni = i + directions[k][0], nj = j + directions[k][1];
            if (ni >= 0 && ni < m && nj >= 0 && nj < n && matrix[ni][nj] >= matrix[i][j]) {
                dfs(matrix, visited, ni, nj);
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
- Use DFS to traverse the grid from the Pacific and Atlantic ocean borders.
- Mark the reachable cells from each ocean using separate boolean matrices.
- Find the common cells that are reachable from both oceans.