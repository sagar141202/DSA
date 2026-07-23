# Pacific Atlantic Water Flow

## Problem Statement
There is a matrix of m x n cells, each cell has a certain height. Water can flow from a cell to its adjacent cells (up, down, left, right) if the adjacent cell has a higher or equal height. There are two oceans, Pacific and Atlantic, and they are located at the borders of the matrix. The Pacific Ocean is located at the top and left borders, while the Atlantic Ocean is located at the bottom and right borders. We need to find all the cells from which water can flow to both oceans.

## Approach
The algorithm uses depth-first search (DFS) to traverse the matrix from the borders. It starts from the Pacific Ocean and marks all the cells that can be reached, then starts from the Atlantic Ocean and marks all the cells that can be reached. The cells that are marked in both traversals are the cells from which water can flow to both oceans.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

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
        
        // traverse from pacific ocean
        for (int i = 0; i < m; i++) {
            dfs(heights, pacific, i, 0);
        }
        for (int j = 0; j < n; j++) {
            dfs(heights, pacific, 0, j);
        }
        
        // traverse from atlantic ocean
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
        vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
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
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

## Key Takeaways
- Use DFS to traverse the matrix from the borders of the oceans.
- Mark the cells that can be reached from each ocean and find the common cells.
- The time complexity is O(m*n) and the space complexity is O(m*n) due to the recursive call stack and the visited matrices.