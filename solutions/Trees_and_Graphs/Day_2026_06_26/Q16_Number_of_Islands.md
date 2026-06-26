# Number of Islands

## Problem Statement
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water. The input grid will be a 2D array of size m x n, where m and n are integers between 1 and 200. Each cell in the grid will be either '0' or '1'. For example, given the following grid:
```
[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
```
The output should be 1, as there is only one island in the given grid.

## Approach
The approach to solve this problem is to use a depth-first search (DFS) algorithm to traverse the grid and count the number of islands. We will iterate over each cell in the grid, and if the cell is a land ('1'), we will perform a DFS to mark all the connected lands as visited.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        // Check if the grid is empty
        if (grid.empty()) {
            return 0;
        }

        int count = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                // If the cell is a land, perform DFS and increment the count
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    count++;
                }
            }
        }
        return count;
    }

    void dfs(vector<vector<char>>& grid, int i, int j) {
        // Check if the cell is within the grid boundaries and is a land
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] != '1') {
            return;
        }

        // Mark the cell as visited
        grid[i][j] = '0';

        // Perform DFS on the adjacent cells
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
- Mark the visited cells to avoid revisiting them.
- The time complexity is O(m*n) as we are visiting each cell at most once.