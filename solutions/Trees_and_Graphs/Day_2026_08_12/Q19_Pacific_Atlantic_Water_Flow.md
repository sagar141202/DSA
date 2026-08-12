# Pacific Atlantic Water Flow

## Problem Statement
There is a matrix of size m x n, representing a map with heights of land. Water can flow from a cell to its neighboring cells if the neighboring cell has a higher or equal height. There are two oceans: the Pacific Ocean and the Atlantic Ocean. The Pacific Ocean is located on the left and top edges of the map, and the Atlantic Ocean is located on the right and bottom edges of the map. We need to find all the cells from which water can flow to both the Pacific Ocean and the Atlantic Ocean. The input is a 2D vector of integers, where each integer represents the height of a cell. The output should be a vector of vectors, where each inner vector contains the coordinates of a cell from which water can flow to both oceans.

## Approach
We will use a depth-first search (DFS) algorithm to traverse the map from the edges of both oceans. We will keep track of the cells that can be reached from each ocean and return the cells that can be reached from both oceans. The DFS will start from the edges of the map and explore all the neighboring cells with a higher or equal height.

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
        
        // DFS from the Pacific Ocean
        for (int i = 0; i < m; i++) {
            dfs(matrix, pacific, i, 0);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, pacific, 0, j);
        }
        
        // DFS from the Atlantic Ocean
        for (int i = 0; i < m; i++) {
            dfs(matrix, atlantic, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, atlantic, m - 1, j);
        }
        
        // Find the cells that can be reached from both oceans
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
        if (visited[i][j]) return;
        visited[i][j] = true;
        
        int m = matrix.size();
        int n = matrix[0].size();
        
        // Explore the neighboring cells
        if (i > 0 && matrix[i - 1][j] >= matrix[i][j]) {
            dfs(matrix, visited, i - 1, j);
        }
        if (i < m - 1 && matrix[i + 1][j] >= matrix[i][j]) {
            dfs(matrix, visited, i + 1, j);
        }
        if (j > 0 && matrix[i][j - 1] >= matrix[i][j]) {
            dfs(matrix, visited, i, j - 1);
        }
        if (j < n - 1 && matrix[i][j + 1] >= matrix[i][j]) {
            dfs(matrix, visited, i, j + 1);
        }
    }
};

```

## Test Cases
```
Input: matrix = [
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

## Key Takeaways
- We use DFS to traverse the map from the edges of both oceans.
- We keep track of the cells that can be reached from each ocean using two separate matrices.
- The cells that can be reached from both oceans are the intersection of the two matrices.