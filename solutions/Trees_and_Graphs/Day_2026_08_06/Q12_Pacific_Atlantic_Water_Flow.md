# Pacific Atlantic Water Flow

## Problem Statement
There is a 2D grid of size m x n, where each cell represents the height of the land. Water can flow from a cell to its neighboring cells if the neighboring cell has a higher or equal height. The Pacific Ocean is on the left and top side of the grid, and the Atlantic Ocean is on the right and bottom side of the grid. Find all the cells where water can flow to both the Pacific and Atlantic Oceans.

## Approach
The problem can be solved by using a depth-first search (DFS) algorithm to traverse the grid from both the Pacific and Atlantic Oceans. We start from the cells that are adjacent to the oceans and mark the cells that can be reached. Then, we find the cells that are common to both sets of reachable cells.

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

        // DFS from Pacific Ocean
        for (int i = 0; i < m; i++) {
            dfs(heights, pacific, i, 0);
        }
        for (int j = 0; j < n; j++) {
            dfs(heights, pacific, 0, j);
        }

        // DFS from Atlantic Ocean
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
        visited[i][j] = true;
        int m = heights.size();
        int n = heights[0].size();
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        for (auto& dir : directions) {
            int x = i + dir.first;
            int y = j + dir.second;
            if (x >= 0 && x < m && y >= 0 && y < n && !visited[x][y] && heights[x][y] >= heights[i][j]) {
                dfs(heights, visited, x, y);
            }
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
- Use DFS to traverse the grid from both oceans.
- Mark the cells that can be reached from each ocean.
- Find the cells that are common to both sets of reachable cells.
- The time complexity is O(m * n) because we visit each cell at most twice.