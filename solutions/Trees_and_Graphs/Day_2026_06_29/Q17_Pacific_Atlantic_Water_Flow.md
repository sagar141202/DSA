# Pacific Atlantic Water Flow

## Problem Statement
Given an m x n matrix of non-negative integers representing the height of each cell in a grid, find the cells from which water can flow to both the Pacific and Atlantic oceans. Water can flow from a cell to another cell if the height of the former is greater than or equal to the height of the latter. The Pacific ocean is on the left and top sides of the grid, and the Atlantic ocean is on the right and bottom sides.

## Approach
We can use a depth-first search (DFS) approach to solve this problem by starting from the Pacific and Atlantic oceans and flowing to the adjacent cells if the height is greater than or equal to the current cell. We keep track of the visited cells to avoid revisiting them.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) {
            return {};
        }

        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<bool>> pacific(m, vector<bool>(n, false));
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));
        vector<vector<int>> result;

        // Pacific DFS
        for (int i = 0; i < m; i++) {
            dfs(matrix, pacific, i, 0);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, pacific, 0, j);
        }

        // Atlantic DFS
        for (int i = 0; i < m; i++) {
            dfs(matrix, atlantic, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, atlantic, m - 1, j);
        }

        // Find common cells
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

        // Up
        if (i > 0 && !visited[i - 1][j] && matrix[i - 1][j] >= matrix[i][j]) {
            dfs(matrix, visited, i - 1, j);
        }

        // Down
        if (i < m - 1 && !visited[i + 1][j] && matrix[i + 1][j] >= matrix[i][j]) {
            dfs(matrix, visited, i + 1, j);
        }

        // Left
        if (j > 0 && !visited[i][j - 1] && matrix[i][j - 1] >= matrix[i][j]) {
            dfs(matrix, visited, i, j - 1);
        }

        // Right
        if (j < n - 1 && !visited[i][j + 1] && matrix[i][j + 1] >= matrix[i][j]) {
            dfs(matrix, visited, i, j + 1);
        }
    }
};
```

## Test Cases
```
Input: [
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

## Key Takeaways
- The key to solving this problem is to use DFS to traverse the grid and mark the cells that can flow to the Pacific and Atlantic oceans.
- We need to start the DFS from the Pacific and Atlantic oceans and flow to the adjacent cells if the height is greater than or equal to the current cell.
- We keep track of the visited cells to avoid revisiting them and to find the common cells that can flow to both oceans.