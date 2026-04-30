# Number of Islands

## Problem Statement
Given an `m x n` 2D binary grid `grid` which represents a map of `'1's` (land) and `'0's` (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

## Approach
The solution uses Depth-First Search (DFS) to traverse the grid and count the number of islands. When a land cell is encountered, it is marked as visited and all its adjacent land cells are recursively visited. The algorithm iterates over each cell in the grid, and for each unvisited land cell, it increments the island count and performs a DFS.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == '1') {
                    // increment island count and perform DFS
                    count++;
                    dfs(grid, i, j);
                }
            }
        }
        return count;
    }
    
    void dfs(vector<vector<char>>& grid, int i, int j) {
        // base case: out of bounds or water cell
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] == '0') {
            return;
        }
        // mark cell as visited
        grid[i][j] = '0';
        // recursively visit adjacent cells
        dfs(grid, i - 1, j); // up
        dfs(grid, i + 1, j); // down
        dfs(grid, i, j - 1); // left
        dfs(grid, i, j + 1); // right
    }
};

int main() {
    Solution solution;
    vector<vector<char>> grid = {
        {'1', '1', '1', '1', '0'},
        {'1', '1', '0', '1', '0'},
        {'1', '1', '0', '0', '0'},
        {'0', '0', '0', '0', '0'}
    };
    cout << "Number of islands: " << solution.numIslands(grid) << endl;
    return 0;
}
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
- Mark visited cells to avoid revisiting them and to prevent counting the same island multiple times.
- The time complexity is O(m * n) because in the worst case, we visit each cell once.