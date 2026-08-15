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
and a word "ABCCED", the function returns true because the word can be found in the grid. However, given a board like:
```
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
```
and a word "SEE", the function returns true, but given a word "ABCB", the function returns false.

## Approach
The algorithm uses a Depth-First Search (DFS) approach to traverse the grid and check if the word exists. It iterates over each cell in the grid and calls the DFS function to check if the word can be formed starting from that cell. The DFS function checks if the current character in the word matches the character in the current cell and then recursively checks the adjacent cells.

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
        // Get the number of rows and columns in the board
        int rows = board.size();
        int cols = board[0].size();
        
        // Define the directions for DFS
        vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        // Function to perform DFS
        bool dfs(int i, int j, int index) {
            // If the current character does not match, return false
            if (board[i][j] != word[index]) {
                return false;
            }
            
            // If the entire word has been found, return true
            if (index == word.size() - 1) {
                return true;
            }
            
            // Mark the current cell as visited
            char temp = board[i][j];
            board[i][j] = '#';
            
            // Perform DFS on adjacent cells
            for (auto& dir : directions) {
                int x = i + dir[0];
                int y = j + dir[1];
                
                // Check if the adjacent cell is within the board
                if (x >= 0 && x < rows && y >= 0 && y < cols) {
                    if (dfs(x, y, index + 1)) {
                        return true;
                    }
                }
            }
            
            // Unmark the current cell
            board[i][j] = temp;
            
            // If no adjacent cell leads to the word, return false
            return false;
        }
        
        // Perform DFS on each cell in the board
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (dfs(i, j, 0)) {
                    return true;
                }
            }
        }
        
        // If no cell leads to the word, return false
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
- The problem can be solved using a Depth-First Search (DFS) approach.
- The DFS function should check if the current character in the word matches the character in the current cell and then recursively check the adjacent cells.
- The time complexity of the solution is O(N * M * 4^L), where N is the number of rows, M is the number of columns, and L is the length of the word.