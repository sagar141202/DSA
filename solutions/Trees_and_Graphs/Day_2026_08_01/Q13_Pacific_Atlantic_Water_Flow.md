# Pacific Atlantic Water Flow

## Problem Statement
There is a matrix of m x n cells, each cell has a certain height. Water can flow from a cell to its adjacent cells (up, down, left, right) if the adjacent cell has a higher or equal height. There are two oceans: Pacific and Atlantic. The Pacific ocean is on the left and top side of the matrix, and the Atlantic ocean is on the right and bottom side. We need to find all the cells that water can flow to both oceans.

## Approach
We will use a Depth-First Search (DFS) algorithm to traverse the matrix from both the Pacific and Atlantic oceans. We will keep track of the cells that can flow to both oceans.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

void dfs(vector<vector<int>>& matrix, vector<vector<bool>>& visited, int i, int j, int prevHeight) {
    if (i < 0 || i >= matrix.size() || j < 0 || j >= matrix[0].size() || visited[i][j] || matrix[i][j] < prevHeight) {
        return;
    }
    visited[i][j] = true;
    dfs(matrix, visited, i - 1, j, matrix[i][j]);
    dfs(matrix, visited, i + 1, j, matrix[i][j]);
    dfs(matrix, visited, i, j - 1, matrix[i][j]);
    dfs(matrix, visited, i, j + 1, matrix[i][j]);
}

vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
    if (matrix.empty() || matrix[0].empty()) {
        return {};
    }
    int m = matrix.size();
    int n = matrix[0].size();
    vector<vector<bool>> pacific(m, vector<bool>(n, false));
    vector<vector<bool>> atlantic(m, vector<bool>(n, false));
    
    for (int i = 0; i < m; i++) {
        dfs(matrix, pacific, i, 0, INT_MIN);
        dfs(matrix, atlantic, i, n - 1, INT_MIN);
    }
    for (int j = 0; j < n; j++) {
        dfs(matrix, pacific, 0, j, INT_MIN);
        dfs(matrix, atlantic, m - 1, j, INT_MIN);
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
```

## Test Cases
```
Input: [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

## Key Takeaways
- Use DFS to traverse the matrix from both oceans.
- Keep track of the cells that can flow to both oceans using two separate visited matrices.
- Combine the results from both oceans to find the cells that can flow to both.