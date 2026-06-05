# Pacific Atlantic Water Flow

## Problem Statement
Given an m x n matrix of non-negative integers representing the height of each cell in a continent, where the Pacific ocean touches the left and top edge, and the Atlantic ocean touches the right and bottom edge. Water can only flow in four directions (up, down, left, right) from a cell to another one with a higher or equal height. Each cell can only be visited once. Return a vector of pairs, where each pair contains the coordinates [i, j] of a cell that can flow to both the Pacific and Atlantic oceans.

## Approach
The approach involves using depth-first search (DFS) to traverse the matrix from both the Pacific and Atlantic oceans. We start from the edges of the matrix and move towards the center, marking the cells that can flow to each ocean. We then find the intersection of the two sets of cells to get the cells that can flow to both oceans.

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
        
        // DFS from Pacific
        for (int i = 0; i < m; i++) {
            dfs(matrix, pacific, i, 0);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, pacific, 0, j);
        }
        
        // DFS from Atlantic
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
        
        visited[i][j] = 1;
        
        // Up
        if (i > 0 && matrix[i - 1][j] >= matrix[i][j] && visited[i - 1][j] == 0) {
            dfs(matrix, visited, i - 1, j);
        }
        
        // Down
        if (i < m - 1 && matrix[i + 1][j] >= matrix[i][j] && visited[i + 1][j] == 0) {
            dfs(matrix, visited, i + 1, j);
        }
        
        // Left
        if (j > 0 && matrix[i][j - 1] >= matrix[i][j] && visited[i][j - 1] == 0) {
            dfs(matrix, visited, i, j - 1);
        }
        
        // Right
        if (j < n - 1 && matrix[i][j + 1] >= matrix[i][j] && visited[i][j + 1] == 0) {
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
- Use DFS to traverse the matrix from both the Pacific and Atlantic oceans.
- Mark the cells that can flow to each ocean and find the intersection of the two sets.
- The time complexity is O(m * n) and the space complexity is O(m * n), where m is the number of rows and n is the number of columns in the matrix.