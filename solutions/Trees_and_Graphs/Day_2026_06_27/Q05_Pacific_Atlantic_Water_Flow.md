# Pacific Atlantic Water Flow

## Problem Statement
There is a rectangular matrix of size m x n, where each cell represents the height of the land. Water can flow from a cell to its adjacent cells (up, down, left, right) if the height of the adjacent cell is greater than or equal to the height of the current cell. There are two oceans: the Pacific Ocean on the left and top sides, and the Atlantic Ocean on the right and bottom sides. We need to find all the cells from which water can flow to both oceans. The input is a 2D vector of integers representing the height of the land, and the output is a vector of pairs representing the coordinates of the cells from which water can flow to both oceans.

## Approach
We will use a depth-first search (DFS) algorithm to traverse the matrix from the Pacific and Atlantic Oceans. We will keep track of the cells that can be reached from both oceans and return their coordinates.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return {};
        
        int m = matrix.size();
        int n = matrix[0].size();
        
        vector<vector<bool>> pacific(m, vector<bool>(n, false));
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));
        
        // DFS from Pacific Ocean
        for (int i = 0; i < m; i++) {
            dfs(matrix, pacific, i, 0);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, pacific, 0, j);
        }
        
        // DFS from Atlantic Ocean
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
        int m = matrix.size();
        int n = matrix[0].size();
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
};

```

## Test Cases
```
Input: 
[[1,2,2,3,5],
 [3,2,3,4,4],
 [2,4,5,3,1],
 [6,7,1,4,5],
 [5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

## Key Takeaways
- Use DFS to traverse the matrix from both oceans.
- Keep track of the cells that can be reached from both oceans.
- Return the coordinates of the cells that can flow to both oceans.