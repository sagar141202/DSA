# Number of Islands

## Problem Statement
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water. The input grid is guaranteed to be a non-empty 2D array, and the number of rows and columns will not exceed 100. For example, given the following grid:
```
11110
11010
11000
00000
```
The output will be 1.

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the grid and count the number of islands. It iterates through each cell in the grid, and if the cell is land, it performs a DFS to mark all adjacent land cells as visited. The number of islands is incremented each time a new land cell is encountered.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;
        int count = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    count++;
                }
            }
        }
        return count;
    }
    
    void dfs(vector<vector<char>>& grid, int i, int j) {
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] != '1') return;
        grid[i][j] = '0';
        dfs(grid, i - 1, j);
        dfs(grid, i + 1, j);
        dfs(grid, i, j - 1);
        dfs(grid, i, j + 1);
    }
};
```

## Test Cases
```
Input: [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

## Key Takeaways
- Use DFS to traverse the grid and count the number of islands.
- Mark visited land cells as '0' to avoid revisiting them.
- Increment the island count each time a new land cell is encountered.