# Pacific Atlantic Water Flow

## Problem Statement
Given an m x n matrix of non-negative integers representing the height of each cell in a grid, find the cells from which water can flow to both the Pacific and Atlantic oceans. Water can flow from a cell to another cell if the height of the latter cell is not less than the height of the former cell. The Pacific ocean is on the left and top sides of the grid, and the Atlantic ocean is on the right and bottom sides of the grid. Return a vector of pairs representing the coordinates of the cells from which water can flow to both oceans.

## Approach
The approach involves using Depth-First Search (DFS) to traverse the grid from both the Pacific and Atlantic oceans. We start from the cells on the borders of the grid and mark the cells that can flow to each ocean. Then, we find the cells that are marked for both oceans.

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
        
        // Initialize vectors to store the cells that can flow to each ocean
        vector<vector<bool>> pacific(m, vector<bool>(n, false));
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));
        
        // Function to perform DFS from a given cell
        function<void(int, int, vector<vector<bool>>&)> dfs = 
            [&](int i, int j, vector<vector<bool>>& ocean) {
                ocean[i][j] = true;
                vector<int> directions = {-1, 0, 1, 0, -1};
                for (int k = 0; k < 4; k++) {
                    int x = i + directions[k];
                    int y = j + directions[k + 1];
                    if (x >= 0 && x < m && y >= 0 && y < n && !ocean[x][y] && heights[x][y] >= heights[i][j]) {
                        dfs(x, y, ocean);
                    }
                }
            };
        
        // Perform DFS from the Pacific ocean
        for (int i = 0; i < m; i++) {
            dfs(i, 0, pacific);
        }
        for (int j = 0; j < n; j++) {
            dfs(0, j, pacific);
        }
        
        // Perform DFS from the Atlantic ocean
        for (int i = 0; i < m; i++) {
            dfs(i, n - 1, atlantic);
        }
        for (int j = 0; j < n; j++) {
            dfs(m - 1, j, atlantic);
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
};
```

## Test Cases
```
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

## Key Takeaways
- Use DFS to traverse the grid from both the Pacific and Atlantic oceans.
- Mark the cells that can flow to each ocean using separate vectors.
- Find the cells that are marked for both oceans to get the final result.
- The time complexity is O(m * n) due to the DFS traversal, and the space complexity is O(m * n) for storing the marked cells.