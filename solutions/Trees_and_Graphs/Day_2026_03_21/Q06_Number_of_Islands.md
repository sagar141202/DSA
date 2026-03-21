# Number of Islands

## Problem Statement
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water. The input grid will be a 2D array of integers where 0 represents water and 1 represents land. The number of islands must be returned. For example, given the following grid:
```
[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
```
The output will be 1.

## Approach
The algorithm uses depth-first search to traverse the grid and count the number of islands. When a land cell is encountered, the algorithm marks all adjacent land cells as visited and increments the island count. This process is repeated until all cells in the grid have been visited.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    void dfs(vector<vector<char>>& grid, int i, int j) {
        // Check if the current cell is within the grid boundaries and is a land cell
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] != '1') {
            return;
        }
        // Mark the current cell as visited
        grid[i][j] = '0';
        // Recursively visit all adjacent land cells
        dfs(grid, i - 1, j); // Up
        dfs(grid, i + 1, j); // Down
        dfs(grid, i, j - 1); // Left
        dfs(grid, i, j + 1); // Right
    }

    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) {
            return 0;
        }
        int count = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                // If the current cell is a land cell, increment the island count and mark all adjacent land cells as visited
                if (grid[i][j] == '1') {
                    count++;
                    dfs(grid, i, j);
                }
            }
        }
        return count;
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
- The algorithm uses depth-first search to traverse the grid and count the number of islands.
- The time complexity is O(m*n) because in the worst case, we need to visit every cell in the grid.
- The space complexity is O(m*n) because in the worst case, the recursive call stack can grow up to the size of the grid.