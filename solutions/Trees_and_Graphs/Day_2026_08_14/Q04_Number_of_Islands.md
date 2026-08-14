# Number of Islands

## Problem Statement
Given a 2D grid consisting of '1's (land) and '0's (water), count the number of islands. An island is a group of connected '1's. The task is to write a function that takes a 2D grid as input and returns the number of islands. The grid can contain multiple islands, and each island can be of any size. The function should handle grids of varying sizes and should be efficient in terms of time and space complexity. For example, given the following grid:
```
[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
```
The output should be 1, because there is only one island in the grid.

## Approach
The algorithm uses depth-first search (DFS) to traverse the grid and count the number of islands. It iterates over each cell in the grid, and if the cell is a '1', it performs a DFS to mark all connected '1's as visited. The number of times a DFS is performed is equal to the number of islands.

## Complexity
- Time: O(M*N)
- Space: O(M*N)

## C++ Solution
```cpp
#include <vector>

class Solution {
public:
    int numIslands(std::vector<std::vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) {
            return 0;
        }

        int count = 0;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == '1') {
                    // Perform DFS to mark all connected '1's as visited
                    dfs(grid, i, j);
                    ++count;
                }
            }
        }
        return count;
    }

private:
    void dfs(std::vector<std::vector<char>>& grid, int i, int j) {
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] != '1') {
            return;
        }

        grid[i][j] = '0'; // Mark as visited

        // Recursively visit all neighboring cells
        dfs(grid, i - 1, j); // Up
        dfs(grid, i + 1, j); // Down
        dfs(grid, i, j - 1); // Left
        dfs(grid, i, j + 1); // Right
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

Input: [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

## Key Takeaways
- The algorithm uses DFS to traverse the grid and count the number of islands.
- The time complexity is O(M*N), where M is the number of rows and N is the number of columns in the grid.
- The space complexity is O(M*N), which is used to store the recursive call stack in the worst case.