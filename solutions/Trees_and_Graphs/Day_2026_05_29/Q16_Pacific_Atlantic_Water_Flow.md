# Pacific Atlantic Water Flow

## Problem Statement
Given an m x n matrix of non-negative integers representing the height of each cell in a grid, find the cells from which water can flow to both the Pacific and Atlantic oceans. Water can flow from a cell to its four neighboring cells (up, down, left, right) if the neighboring cell has a higher or equal height. The Pacific ocean is on the left and top side of the grid, and the Atlantic ocean is on the right and bottom side of the grid.

## Approach
The algorithm uses depth-first search (DFS) to traverse the grid from both the Pacific and Atlantic sides, marking the cells that can flow to each ocean. Then, it finds the intersection of these two sets of cells.

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
        
        vector<vector<int>> pacific(m, vector<int>(n, 0));
        vector<vector<int>> atlantic(m, vector<int>(n, 0));
        
        // DFS from Pacific side
        for (int i = 0; i < m; i++) {
            dfs(matrix, pacific, i, 0);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, pacific, 0, j);
        }
        
        // DFS from Atlantic side
        for (int i = 0; i < m; i++) {
            dfs(matrix, atlantic, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, atlantic, m - 1, j);
        }
        
        vector<vector<int>> result;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] == 1 && atlantic[i][j] == 1) {
                    result.push_back({i, j});
                }
            }
        }
        
        return result;
    }
    
    void dfs(vector<vector<int>>& matrix, vector<vector<int>>& visited, int i, int j) {
        int m = matrix.size();
        int n = matrix[0].size();
        
        if (visited[i][j] == 1) return;
        
        visited[i][j] = 1;
        
        int directions[][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        for (auto& direction : directions) {
            int x = i + direction[0];
            int y = j + direction[1];
            
            if (x >= 0 && x < m && y >= 0 && y < n && matrix[x][y] >= matrix[i][j]) {
                dfs(matrix, visited, x, y);
            }
        }
    }
};

```

## Test Cases
```
Input: 
[[1,2,2,3,5],
 [3,2,3,4,4],
 [2,4,5,3,1],
 [6,7,1,4,5],
 [5,1,1,2,4]]

Output: 
[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

## Key Takeaways
- Use DFS to traverse the grid from both the Pacific and Atlantic sides.
- Mark the cells that can flow to each ocean using separate matrices.
- Find the intersection of the two sets of cells to get the final result.
- Use a recursive DFS function to simplify the code and improve readability.