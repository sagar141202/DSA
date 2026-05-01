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
and word = "ABCCED", the function returns true because the word can be found in the grid. However, if the word is "SEE", the function returns true, but if the word is "ABCB", the function returns false.

## Approach
The algorithm uses a depth-first search (DFS) approach to explore all possible paths in the grid. It checks each cell in the grid to see if it matches the first letter of the word, and then recursively checks adjacent cells to see if they match the next letter in the word. The search is case-sensitive and only considers horizontal and vertical movements.

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
        
        // Define the possible movements (up, down, left, right)
        vector<int> dx = {-1, 1, 0, 0};
        vector<int> dy = {0, 0, -1, 1};
        
        // Function to perform DFS
        function<bool(int, int, int)> dfs = 
            [&](int x, int y, int index) {
                // If we've reached the end of the word, return true
                if (index == word.size()) return true;
                
                // If the current cell is out of bounds or doesn't match the current letter, return false
                if (x < 0 || x >= rows || y < 0 || y >= cols || word[index] != board[x][y]) return false;
                
                // Mark the current cell as visited
                char temp = board[x][y];
                board[x][y] = '#';
                
                // Recursively check all adjacent cells
                for (int i = 0; i < 4; i++) {
                    if (dfs(x + dx[i], y + dy[i], index + 1)) return true;
                }
                
                // Unmark the current cell
                board[x][y] = temp;
                
                // If no adjacent cell leads to a solution, return false
                return false;
            };
        
        // Check all cells in the board
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (dfs(i, j, 0)) return true;
            }
        }
        
        // If no cell leads to a solution, return false
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
- Use DFS to explore all possible paths in the grid.
- Mark visited cells to avoid revisiting them and to ensure that the same letter cell is not used more than once.
- Unmark visited cells after exploring all adjacent cells to restore the original state of the board.