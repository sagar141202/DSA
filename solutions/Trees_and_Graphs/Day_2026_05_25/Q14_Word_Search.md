# Word Search

## Problem Statement
Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once. For example, given a board like:
```
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
```
and a word like "ABCCED", the function should return true because the word can be found in the grid.

## Approach
The algorithm uses a depth-first search (DFS) approach to explore all possible paths from each cell in the grid. It checks if the current character in the word matches the character in the current cell and then recursively checks the adjacent cells.

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
        // Get the dimensions of the board
        int rows = board.size();
        int cols = board[0].size();
        
        // Define the directions for DFS
        vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        // Function to check if a cell is within the board
        auto isValid = [&](int x, int y) {
            return x >= 0 && x < rows && y >= 0 && y < cols;
        };
        
        // DFS function to check if the word exists
        function<bool(int, int, int)> dfs = [&](int x, int y, int index) {
            // If the index is equal to the length of the word, return true
            if (index == word.size()) return true;
            
            // If the current character does not match, return false
            if (board[x][y] != word[index]) return false;
            
            // Mark the current cell as visited
            char temp = board[x][y];
            board[x][y] = '#';
            
            // Check all adjacent cells
            for (auto [dx, dy] : directions) {
                int nx = x + dx;
                int ny = y + dy;
                
                // If the adjacent cell is valid and the DFS returns true, return true
                if (isValid(nx, ny) && dfs(nx, ny, index + 1)) return true;
            }
            
            // Unmark the current cell
            board[x][y] = temp;
            
            // If no adjacent cell returns true, return false
            return false;
        };
        
        // Check all cells in the board
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // If the DFS returns true, return true
                if (dfs(i, j, 0)) return true;
            }
        }
        
        // If no cell returns true, return false
        return false;
    }
};
```

## Test Cases
```
Input: board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], word = "ABCCED"
Output: true

Input: board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], word = "SEE"
Output: true

Input: board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], word = "ABCB"
Output: false
```

## Key Takeaways
- Use a depth-first search approach to explore all possible paths from each cell in the grid.
- Use a function to check if a cell is within the board to avoid out-of-bounds errors.
- Use a function to perform the DFS and check if the word exists in the grid.