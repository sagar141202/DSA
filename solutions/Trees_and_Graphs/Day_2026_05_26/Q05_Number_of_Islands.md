# Number of Islands

## Problem Statement
Given a 2D grid consisting of '1's (land) and '0's (water), count the number of islands. An island is a group of connected '1's. The task is to write a function that takes a 2D grid as input and returns the number of islands. The grid can contain any number of islands, and the islands can be of any shape or size. For example, given the grid:
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
The approach to solve this problem is to use depth-first search (DFS) to traverse the grid and count the number of islands. We iterate over each cell in the grid, and if the cell is '1', we perform a DFS to mark all connected '1's as visited.

## Complexity
- Time: O(M*N)
- Space: O(M*N)

## C++ Solution
```cpp
#include <vector>

class Solution {
public:
    int numIslands(std::vector<std::vector<char>>& grid) {
        if (grid.empty()) {
            return 0;
        }

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

    void dfs(std::vector<std::vector<char>>& grid, int i, int j) {
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] != '1') {
            return;
        }
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

Input: [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

## Key Takeaways
- Use DFS to traverse the grid and count the number of islands.
- Mark visited cells as '0' to avoid revisiting them.
- The time complexity is O(M*N) because we visit each cell at most once.