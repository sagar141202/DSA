# Pacific Atlantic Water Flow

## Problem Statement
There is a matrix of size m x n, representing a piece of land with heights. Water can flow from each cell to its four adjacent cells (up, down, left, right) if the height of the adjacent cell is greater than or equal to the height of the current cell. There are two oceans, Pacific and Atlantic, which are located at the left/right and top/bottom borders of the matrix respectively. We need to find all the cells from which water can flow to both oceans.

## Approach
The approach is to use depth-first search (DFS) to traverse the matrix from the borders of the Pacific and Atlantic oceans. We will keep track of the cells that can flow to each ocean and then find the intersection of these two sets of cells.

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
        
        // DFS from Pacific
        for (int i = 0; i < m; i++) {
            dfs(heights, pacific, i, 0);
        }
        for (int j = 0; j < n; j++) {
            dfs(heights, pacific, 0, j);
        }
        
        // DFS from Atlantic
        for (int i = 0; i < m; i++) {
            dfs(heights, atlantic, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            dfs(heights, atlantic, m - 1, j);
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
    
    void dfs(vector<vector<int>>& heights, vector<vector<bool>>& visited, int i, int j) {
        int m = heights.size();
        int n = heights[0].size();
        visited[i][j] = true;
        
        // Up
        if (i - 1 >= 0 && !visited[i - 1][j] && heights[i - 1][j] >= heights[i][j]) {
            dfs(heights, visited, i - 1, j);
        }
        // Down
        if (i + 1 < m && !visited[i + 1][j] && heights[i + 1][j] >= heights[i][j]) {
            dfs(heights, visited, i + 1, j);
        }
        // Left
        if (j - 1 >= 0 && !visited[i][j - 1] && heights[i][j - 1] >= heights[i][j]) {
            dfs(heights, visited, i, j - 1);
        }
        // Right
        if (j + 1 < n && !visited[i][j + 1] && heights[i][j + 1] >= heights[i][j]) {
            dfs(heights, visited, i, j + 1);
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
- Use DFS to traverse the matrix from the borders of the Pacific and Atlantic oceans.
- Keep track of the cells that can flow to each ocean using separate boolean matrices.
- Find the intersection of the two sets of cells to get the final result.