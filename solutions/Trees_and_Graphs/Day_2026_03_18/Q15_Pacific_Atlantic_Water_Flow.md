# Pacific Atlantic Water Flow

## Problem Statement
Given an `m x n` matrix of non-negative integers representing the height of each cell in a grid, find the cells from which water can flow to both the Pacific and Atlantic oceans. Water can flow from a cell to another cell if the height of the destination cell is greater than or equal to the height of the source cell. The Pacific ocean is on the left and top edges of the grid, and the Atlantic ocean is on the right and bottom edges. Return a vector of vectors, where each inner vector contains two integers representing the row and column of a cell from which water can flow to both oceans. The input grid will have at least one cell, and the number of cells will not exceed 5 * 10^5. The height of each cell will be in the range [0, 10^5].

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the grid from both the Pacific and Atlantic oceans. It maintains two separate sets to keep track of the cells that can flow to each ocean. The DFS is performed from the edges of the grid, and the cells that can flow to both oceans are added to the result set.

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
        
        vector<vector<int>> result;
        vector<vector<bool>> pacific(m, vector<bool>(n, false));
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));
        
        // Perform DFS from the Pacific ocean
        for (int i = 0; i < m; i++) {
            dfs(matrix, pacific, i, 0);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, pacific, 0, j);
        }
        
        // Perform DFS from the Atlantic ocean
        for (int i = 0; i < m; i++) {
            dfs(matrix, atlantic, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, atlantic, m - 1, j);
        }
        
        // Find the cells that can flow to both oceans
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
        
        // Explore the neighbors
        vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (auto& direction : directions) {
            int x = i + direction[0];
            int y = j + direction[1];
            
            if (x >= 0 && x < m && y >= 0 && y < n && !visited[x][y] && matrix[x][y] >= matrix[i][j]) {
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
- The DFS approach is used to traverse the grid from both the Pacific and Atlantic oceans.
- Two separate sets are maintained to keep track of the cells that can flow to each ocean.
- The cells that can flow to both oceans are added to the result set by checking the intersection of the two sets.