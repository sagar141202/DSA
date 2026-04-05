# Pacific Atlantic Water Flow

## Problem Statement
Given an m x n matrix of non-negative integers representing the height of each cell in a grid, find the cells from which water can flow to both the Pacific and Atlantic oceans. Water can flow from a cell to another cell if the height of the second cell is not less than the height of the first cell. The Pacific ocean is on the left and top side of the grid, and the Atlantic ocean is on the right and bottom side of the grid. Return a vector of vectors, where each vector contains the coordinates of a cell from which water can flow to both oceans.

## Approach
The algorithm uses depth-first search (DFS) to traverse the grid and find the cells that can flow to both oceans. It starts from the Pacific and Atlantic coasts and marks the cells that can flow to each ocean. Then, it finds the cells that are marked for both oceans.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size();
        int n = heights[0].size();
        vector<vector<bool>> pacific(m, vector<bool>(n, false));
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));
        
        // DFS from Pacific coast
        for (int i = 0; i < m; i++) {
            dfs(heights, pacific, i, 0);
        }
        for (int j = 0; j < n; j++) {
            dfs(heights, pacific, 0, j);
        }
        
        // DFS from Atlantic coast
        for (int i = 0; i < m; i++) {
            dfs(heights, atlantic, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            dfs(heights, atlantic, m - 1, j);
        }
        
        // Find cells that can flow to both oceans
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
    
    void dfs(vector<vector<int>>& heights, vector<vector<bool>>& visited, int i, int j) {
        int m = heights.size();
        int n = heights[0].size();
        if (i < 0 || i >= m || j < 0 || j >= n || visited[i][j]) {
            return;
        }
        visited[i][j] = true;
        if (i > 0 && heights[i - 1][j] >= heights[i][j]) {
            dfs(heights, visited, i - 1, j);
        }
        if (i < m - 1 && heights[i + 1][j] >= heights[i][j]) {
            dfs(heights, visited, i + 1, j);
        }
        if (j > 0 && heights[i][j - 1] >= heights[i][j]) {
            dfs(heights, visited, i, j - 1);
        }
        if (j < n - 1 && heights[i][j + 1] >= heights[i][j]) {
            dfs(heights, visited, i, j + 1);
        }
    }
};

```

## Test Cases
```
Input: heights = [
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

## Key Takeaways
- Use DFS to traverse the grid and mark the cells that can flow to each ocean.
- Start DFS from the coast of each ocean to find the cells that can flow to that ocean.
- Find the cells that are marked for both oceans to get the final result.