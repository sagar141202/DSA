# Word Search

## Problem Statement
Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once. For example, given a board `[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]` and a word `"ABCCED"`, the word exists in the grid.

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the grid and check if the word can be formed. It starts from each cell in the grid and checks if the current character in the word matches the character in the cell. If it does, it recursively checks the adjacent cells for the next character in the word.

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
        
        // Define the possible directions for DFS
        vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        // Function to perform DFS
        bool dfs(int row, int col, int index) {
            // If the current index is equal to the length of the word, return true
            if (index == word.size()) return true;
            
            // If the current cell is out of bounds or the character does not match, return false
            if (row < 0 || row >= rows || col < 0 || col >= cols || word[index] != board[row][col]) return false;
            
            // Mark the current cell as visited
            char temp = board[row][col];
            board[row][col] = '#';
            
            // Perform DFS in all possible directions
            for (auto& dir : directions) {
                if (dfs(row + dir[0], col + dir[1], index + 1)) return true;
            }
            
            // Unmark the current cell
            board[row][col] = temp;
            
            // If no direction leads to a solution, return false
            return false;
        }
        
        // Perform DFS from each cell in the board
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (dfs(i, j, 0)) return true;
            }
        }
        
        // If no solution is found, return false
        return false;
    }
};
```

## Test Cases
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

## Key Takeaways
- Use DFS to traverse the grid and check if the word can be formed.
- Mark visited cells to avoid revisiting them and to ensure that each cell is used only once.
- Perform DFS in all possible directions from each cell to cover all possible paths.