# Pacific Atlantic Water Flow

## Problem Statement
There is a 2D grid of size m x n, representing a map with elevations. Water can flow from a cell to its adjacent cells (up, down, left, right) if the elevation of the adjacent cell is greater than or equal to the elevation of the current cell. There are two oceans: Pacific and Atlantic. The Pacific Ocean is on the left and top sides of the grid, while the Atlantic Ocean is on the right and bottom sides. We need to find all cells from which water can flow to both the Pacific and Atlantic Oceans.

## Approach
We will use a Depth-First Search (DFS) approach to traverse the grid and find cells that can flow to both oceans. We will start from the cells on the borders of the grid and perform DFS to mark all reachable cells.

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
        
        // Perform DFS from Pacific Ocean
        for (int i = 0; i < m; i++) {
            dfs(heights, pacific, i, 0);
        }
        for (int j = 0; j < n; j++) {
            dfs(heights, pacific, 0, j);
        }
        
        // Perform DFS from Atlantic Ocean
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
        if (visited[i][j]) return;
        visited[i][j] = true;
        int m = heights.size();
        int n = heights[0].size();
        int directions[][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (int k = 0; k < 4; k++) {
            int ni = i + directions[k][0];
            int nj = j + directions[k][1];
            if (ni >= 0 && ni < m && nj >= 0 && nj < n && heights[ni][nj] >= heights[i][j]) {
                dfs(heights, visited, ni, nj);
            }
        }
    }
};

```

## Test Cases
```
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

## Key Takeaways
- Use DFS to traverse the grid and find cells that can flow to both oceans.
- Start from the cells on the borders of the grid and perform DFS to mark all reachable cells.
- Use two separate boolean matrices to keep track of cells that can flow to the Pacific and Atlantic Oceans.