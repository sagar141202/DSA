# Pacific Atlantic Water Flow

## Problem Statement
Given an `m x n` matrix of non-negative integers representing the height of each cell in a grid, find the cells from which water can flow to both the Pacific and Atlantic oceans. Water can flow from a cell to another cell if the height of the second cell is not less than the height of the first cell. The Pacific ocean is on the left and top sides of the grid, and the Atlantic ocean is on the right and bottom sides. Return a vector of vectors, where each inner vector contains two integers representing the row and column indices of the cells from which water can flow to both oceans. The input grid will have at least one cell, and the number of cells will not exceed 5 * 10^4.

## Approach
The approach involves using depth-first search (DFS) to traverse the grid from both the Pacific and Atlantic oceans. We start from the cells on the borders of the grid and mark the cells that can flow to each ocean. Then, we find the intersection of the cells that can flow to both oceans.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
    if (matrix.empty() || matrix[0].empty()) return {};

    int m = matrix.size();
    int n = matrix[0].size();
    vector<vector<bool>> pacific(m, vector<bool>(n, false));
    vector<vector<bool>> atlantic(m, vector<bool>(n, false));

    // DFS from Pacific
    for (int i = 0; i < m; i++) {
        dfs(matrix, pacific, i, 0, matrix[i][0]);
    }
    for (int j = 0; j < n; j++) {
        dfs(matrix, pacific, 0, j, matrix[0][j]);
    }

    // DFS from Atlantic
    for (int i = 0; i < m; i++) {
        dfs(matrix, atlantic, i, n - 1, matrix[i][n - 1]);
    }
    for (int j = 0; j < n; j++) {
        dfs(matrix, atlantic, m - 1, j, matrix[m - 1][j]);
    }

    // Find intersection
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

void dfs(vector<vector<int>>& matrix, vector<vector<bool>>& visited, int i, int j, int height) {
    if (i < 0 || i >= matrix.size() || j < 0 || j >= matrix[0].size() || visited[i][j] || matrix[i][j] < height) return;
    visited[i][j] = true;
    dfs(matrix, visited, i - 1, j, matrix[i][j]);
    dfs(matrix, visited, i + 1, j, matrix[i][j]);
    dfs(matrix, visited, i, j - 1, matrix[i][j]);
    dfs(matrix, visited, i, j + 1, matrix[i][j]);
}
```

## Test Cases
```
Input: [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

## Key Takeaways
- Use DFS to traverse the grid from both the Pacific and Atlantic oceans.
- Mark the cells that can flow to each ocean using separate matrices.
- Find the intersection of the cells that can flow to both oceans to get the final result.
- The time complexity is O(m * n) where m and n are the dimensions of the grid.