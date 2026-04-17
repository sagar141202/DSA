# Pacific Atlantic Water Flow

## Problem Statement
There is a rectangular matrix of m x n size, representing a map with heights of each cell. Each cell can flow water to its adjacent cells (up, down, left, right) if the height of the adjacent cell is greater than or equal to the height of the current cell. There are two oceans, the Pacific and the Atlantic. The Pacific Ocean is on the left and top edges of the map, and the Atlantic Ocean is on the right and bottom edges. Find all the cells that can flow to both the Pacific and the Atlantic Oceans. The input will be a 2D vector of integers representing the heights of each cell. The output should be a vector of pairs, where each pair contains the row and column of a cell that can flow to both oceans.

## Approach
The algorithm uses depth-first search (DFS) to traverse the matrix from both the Pacific and Atlantic Oceans. It keeps track of the cells that can flow to each ocean and returns the intersection of these two sets. The DFS traversal is performed from the boundary cells of the oceans.

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
        
        // Perform DFS from the Pacific Ocean
        for (int i = 0; i < m; i++) {
            dfs(matrix, pacific, i, 0);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, pacific, 0, j);
        }
        
        // Perform DFS from the Atlantic Ocean
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
        
        // Explore adjacent cells
        int directions[][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        for (int k = 0; k < 4; k++) {
            int ni = i + directions[k][0];
            int nj = j + directions[k][1];
            
            if (ni >= 0 && ni < m && nj >= 0 && nj < n && !visited[ni][nj] && matrix[ni][nj] >= matrix[i][j]) {
                dfs(matrix, visited, ni, nj);
            }
        }
    }
};
```

## Test Cases
```
Input: [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

## Key Takeaways
- The problem can be solved using DFS traversal from the boundary cells of the oceans.
- The time complexity is O(m * n) because we are visiting each cell at most twice (once from the Pacific and once from the Atlantic).
- The space complexity is O(m * n) because we need to store the visited cells for both oceans.