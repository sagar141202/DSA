# Number of Islands

## Problem Statement
Given a 2D grid consisting of '1's (land) and '0's (water), count the number of islands. An island is a group of connected '1's. The task is to write a function that takes a 2D grid as input and returns the number of islands. The grid can contain multiple islands, and each island can be of any shape or size. The function should be able to handle grids of varying sizes and should be efficient in terms of time and space complexity. For example, given the following grid:
```
11110
11010
11000
00000
```
The function should return 1, because there is only one island.

## Approach
The approach to solve this problem is to use a depth-first search (DFS) algorithm to traverse the grid and count the number of islands. We will iterate over each cell in the grid, and if we encounter a '1', we will perform a DFS from that cell to mark all connected '1's as visited.

## Complexity
- Time: O(M*N)
- Space: O(M*N)

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
                    // Perform DFS from this cell
                    dfs(grid, i, j);
                    count++;
                }
            }
        }
        return count;
    }
    
    void dfs(vector<vector<char>>& grid, int i, int j) {
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] != '1') {
            return;
        }
        grid[i][j] = '0'; // Mark as visited
        dfs(grid, i - 1, j); // Up
        dfs(grid, i + 1, j); // Down
        dfs(grid, i, j - 1); // Left
        dfs(grid, i, j + 1); // Right
    }
};
```

## Test Cases
```
Input: 
[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Input: 
[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

## Key Takeaways
- The DFS approach is suitable for this problem because it allows us to traverse the grid and mark connected '1's as visited efficiently.
- The time complexity is O(M*N) because we visit each cell in the grid once.
- The space complexity is O(M*N) because in the worst case, we might need to store all cells in the call stack during the DFS traversal.