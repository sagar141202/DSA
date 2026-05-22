# Pacific Atlantic Water Flow

## Problem Statement
There is a rectangular grid map where each cell represents the height of the land. Water can flow from any cell to its adjacent cells (up, down, left, right) if the adjacent cell has a higher or equal height. There are two oceans: Pacific and Atlantic. The Pacific Ocean is on the left and top edges of the map, and the Atlantic Ocean is on the right and bottom edges. Given the grid map, find all the cells that water can flow from to both the Pacific and Atlantic oceans. The input is a 2D vector of integers representing the height of the land in each cell. The output should be a vector of pairs, where each pair represents the coordinates of a cell that can flow to both oceans.

## Approach
We will use a depth-first search (DFS) algorithm to traverse the grid from the Pacific and Atlantic oceans. We will start from the edges of the grid and mark all the cells that can flow to each ocean. Then, we will find the intersection of the two sets of cells to get the cells that can flow to both oceans.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

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
    
    // mark cells that can flow to Pacific
    for (int i = 0; i < m; i++) {
        dfs(matrix, pacific, i, 0, INT_MIN);
    }
    for (int j = 0; j < n; j++) {
        dfs(matrix, pacific, 0, j, INT_MIN);
    }
    
    // mark cells that can flow to Atlantic
    for (int i = 0; i < m; i++) {
        dfs(matrix, atlantic, i, n - 1, INT_MIN);
    }
    for (int j = 0; j < n; j++) {
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
- Use DFS to traverse the grid from the edges of the Pacific and Atlantic oceans.
- Mark cells that can flow to each ocean and find the intersection of the two sets of cells.
- The time complexity is O(m*n) because we visit each cell at most once for each ocean.