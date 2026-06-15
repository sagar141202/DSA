# Word Search

## Problem Statement
Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once. For example, given the following board and word:
```
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
```
and word `ABCCED`, the function returns `true` because the word can be found in the grid.

## Approach
The algorithm uses a depth-first search (DFS) to traverse the grid and check if the word can be formed. It iterates over each cell in the grid, and for each cell, it checks if the current character in the word matches the character in the cell. If it does, it recursively calls the DFS function for the adjacent cells.

## Complexity
- Time: O(N * M * 4^L)
- Space: O(N * M + L)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        // Get the number of rows and columns in the grid
        int rows = board.size();
        int cols = board[0].size();
        
        // Define the directions for DFS
        vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        // Function to perform DFS
        function<bool(int, int, int)> dfs = [&](int i, int j, int k) {
            // If we have found the entire word, return true
            if (k == word.size()) return true;
            
            // If the current character does not match, return false
            if (board[i][j] != word[k]) return false;
            
            // Mark the current cell as visited
            char temp = board[i][j];
            board[i][j] = '#';
            
            // Perform DFS for the adjacent cells
            for (auto& dir : directions) {
                int x = i + dir.first;
                int y = j + dir.second;
                
                // Check if the adjacent cell is within the grid
                if (x >= 0 && x < rows && y >= 0 && y < cols) {
                    if (dfs(x, y, k + 1)) return true;
                }
            }
            
            // Unmark the current cell
            board[i][j] = temp;
            
            // If we have not found the word, return false
            return false;
        };
        
        // Perform DFS for each cell in the grid
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (dfs(i, j, 0)) return true;
            }
        }
        
        // If we have not found the word, return false
        return false;
    }
};
```

## Test Cases
```
Input: 
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
Output: true

Input: 
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "SEE"
Output: true

Input: 
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCB"
Output: false
```

## Key Takeaways
- Use DFS to traverse the grid and check if the word can be formed.
- Mark the current cell as visited to avoid revisiting it.
- Unmark the current cell after visiting its adjacent cells to allow other paths to visit it.
- Perform DFS for each cell in the grid to ensure that we do not miss any possible paths.