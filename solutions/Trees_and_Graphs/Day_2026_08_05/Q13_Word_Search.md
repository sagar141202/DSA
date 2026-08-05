# Word Search

## Problem Statement
Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once. For example, given a board `[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]` and a word `"ABCCED"`, the word exists in the grid.

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the grid and check if the word can be formed. It iterates over each cell in the grid and checks if the current cell matches the first character of the word. If it does, it calls the DFS function to check if the rest of the word can be formed.

## Complexity
- Time: O(N*M*4^L)
- Space: O(N*M + L)

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
        vector<int> dx = {0, 0, 1, -1};
        vector<int> dy = {1, -1, 0, 0};
        
        // Function to perform DFS
        function<bool(int, int, int)> dfs = 
            [&](int x, int y, int index) {
                // If the current character does not match, return false
                if (board[x][y] != word[index]) return false;
                
                // If the entire word has been found, return true
                if (index == word.size() - 1) return true;
                
                // Mark the current cell as visited
                char temp = board[x][y];
                board[x][y] = '#';
                
                // Perform DFS in all four directions
                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    
                    // Check if the new cell is within the grid
                    if (nx >= 0 && nx < rows && ny >= 0 && ny < cols) {
                        // If DFS returns true, return true
                        if (dfs(nx, ny, index + 1)) return true;
                    }
                }
                
                // Unmark the current cell
                board[x][y] = temp;
                
                // If no path is found, return false
                return false;
            };
        
        // Perform DFS from each cell in the grid
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (dfs(i, j, 0)) return true;
            }
        }
        
        // If no path is found, return false
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
- Mark visited cells to avoid revisiting them and to ensure that the same letter cell is not used more than once.
- Unmark visited cells after exploring all possible paths from a cell.