# Pacific Atlantic Water Flow

## Problem Statement
There is a matrix of m x n cells, where each cell has a certain height. Water can flow from a cell to its adjacent cells (up, down, left, right) if the adjacent cell has a greater or equal height. We need to find all cells from which water can flow to both the Pacific and the Atlantic oceans. The Pacific ocean is on the left and top sides of the matrix, and the Atlantic ocean is on the right and bottom sides. The input is a 2D array of integers, where each integer represents the height of a cell. The output should be a vector of pairs, where each pair contains the row and column indices of a cell from which water can flow to both oceans.

## Approach
We can use a depth-first search (DFS) algorithm to solve this problem. We start by performing DFS from the Pacific and Atlantic oceans, marking all cells that can flow to each ocean. Then, we find the cells that are marked for both oceans.

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
        
        if (i < 0 || i >= m || j < 0 || j >= n || visited[i][j]) return;
        
        visited[i][j] = true;
        
        // Perform DFS on adjacent cells
        if (i > 0 && matrix[i - 1][j] >= matrix[i][j]) {
            dfs(matrix, visited, i - 1, j);
        }
        if (i < m - 1 && matrix[i + 1][j] >= matrix[i][j]) {
            dfs(matrix, visited, i + 1, j);
        }
        if (j > 0 && matrix[i][j - 1] >= matrix[i][j]) {
            dfs(matrix, visited, i, j - 1);
        }
        if (j < n - 1 && matrix[i][j + 1] >= matrix[i][j]) {
            dfs(matrix, visited, i, j + 1);
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
- Use DFS to mark cells that can flow to each ocean.
- Perform DFS from the Pacific and Atlantic oceans separately.
- Find the cells that are marked for both oceans.