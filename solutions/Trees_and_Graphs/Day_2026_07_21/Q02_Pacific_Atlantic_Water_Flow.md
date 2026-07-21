# Pacific Atlantic Water Flow

## Problem Statement
There is a rectangular matrix of m x n cells, each cell has a certain height. Water can flow from a cell to its four neighboring cells (up, down, left, right) if the neighboring cell's height is greater than or equal to the current cell's height. The Pacific Ocean is on the left and top side of the matrix, and the Atlantic Ocean is on the right and bottom side. We need to find all cells that water can flow to both the Pacific and Atlantic Oceans. The input is a 2D vector of integers representing the height of each cell. The output should be a vector of vectors, where each inner vector contains the row and column of a cell that water can flow to both oceans. 1 <= m, n <= 200, and 0 <= height[i][j] <= 10^5.

## Approach
We will use a depth-first search (DFS) algorithm to traverse the matrix from both the Pacific and Atlantic Oceans. We will keep track of the cells that can flow to both oceans. The key idea is to start the DFS from the boundary cells of both oceans and mark the cells that can flow to each ocean.

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
    
    // DFS from Pacific Ocean
    for (int i = 0; i < m; i++) {
        dfs(matrix, pacific, matrix[0][0], i, 0);
    }
    for (int j = 0; j < n; j++) {
        dfs(matrix, pacific, matrix[0][0], 0, j);
    }
    
    // DFS from Atlantic Ocean
    for (int i = 0; i < m; i++) {
        dfs(matrix, atlantic, matrix[m - 1][n - 1], i, n - 1);
    }
    for (int j = 0; j < n; j++) {
        dfs(matrix, atlantic, matrix[m - 1][n - 1], m - 1, j);
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

void dfs(vector<vector<int>>& matrix, vector<vector<bool>>& visited, int height, int i, int j) {
    int m = matrix.size();
    int n = matrix[0].size();
    
    if (i < 0 || i >= m || j < 0 || j >= n || visited[i][j] || matrix[i][j] < height) return;
    
    visited[i][j] = true;
    
    dfs(matrix, visited, matrix[i][j], i - 1, j);
    dfs(matrix, visited, matrix[i][j], i + 1, j);
    dfs(matrix, visited, matrix[i][j], i, j - 1);
    dfs(matrix, visited, matrix[i][j], i, j + 1);
}
```

## Test Cases
```
Input: [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

## Key Takeaways
- Use DFS to traverse the matrix from both oceans.
- Keep track of the cells that can flow to both oceans.
- Use a separate visited matrix for each ocean to avoid overwriting the results.