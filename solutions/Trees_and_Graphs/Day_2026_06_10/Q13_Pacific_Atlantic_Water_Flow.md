# Pacific Atlantic Water Flow

## Problem Statement
Given an m x n matrix of non-negative integers representing the height of each cell in a grid, find the cells from which water can flow to both the Pacific and Atlantic oceans. Water can flow from a cell to another cell if the height of the former cell is greater than or equal to the height of the latter cell. The Pacific ocean is on the left and top sides of the grid, and the Atlantic ocean is on the right and bottom sides. Return a vector of pairs, where each pair contains the row and column indices of the cells from which water can flow to both oceans. The input grid will have at least one cell, and the number of cells will not exceed 5 * 10^5.

## Approach
The algorithm uses depth-first search (DFS) to traverse the grid from the Pacific and Atlantic oceans. It keeps track of the cells that can flow to each ocean and returns the intersection of these sets. The DFS traversal is performed from the boundary cells of the grid.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
    if (matrix.empty() || matrix[0].empty()) return {};

    int m = matrix.size(), n = matrix[0].size();
    vector<vector<bool>> pacific(m, vector<bool>(n, false));
    vector<vector<bool>> atlantic(m, vector<bool>(n, false));

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
            if (pacific[i][j] && atlantic[i][j]) {
                result.push_back({i, j});
            }
        }
    }
    return result;
}

void dfs(vector<vector<int>>& matrix, vector<vector<bool>>& visited, int i, int j) {
    int m = matrix.size(), n = matrix[0].size();
    visited[i][j] = true;
    vector<int> dx = {-1, 1, 0, 0};
    vector<int> dy = {0, 0, -1, 1};

    for (int k = 0; k < 4; k++) {
        int x = i + dx[k];
        int y = j + dy[k];
        if (x >= 0 && x < m && y >= 0 && y < n && !visited[x][y] && matrix[x][y] >= matrix[i][j]) {
            dfs(matrix, visited, x, y);
        }
    }
}

int main() {
    vector<vector<int>> matrix = {
        {1, 2, 2, 3, 5},
        {3, 2, 3, 4, 4},
        {2, 4, 5, 3, 1},
        {6, 7, 1, 4, 5},
        {5, 1, 1, 2, 4}
    };
    vector<vector<int>> result = pacificAtlantic(matrix);
    for (auto& vec : result) {
        cout << "(" << vec[0] << ", " << vec[1] << ") ";
    }
    return 0;
}
```

## Test Cases
```
Input: 
[
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]
Output: [(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)]
```

## Key Takeaways
- Use DFS to traverse the grid from the Pacific and Atlantic oceans.
- Keep track of the cells that can flow to each ocean using separate matrices.
- Return the intersection of the sets of cells that can flow to both oceans.
- The time complexity is O(m * n) due to the DFS traversal, and the space complexity is O(m * n) for the visited matrices.