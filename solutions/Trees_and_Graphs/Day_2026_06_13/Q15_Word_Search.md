# Word Search

## Problem Statement
Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once. For example, given a 2D board containing the letters [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ] and the word "ABCCED", the function should return true because the word can be found in the grid. However, if the word is "SEE", the function should return true, and if the word is "ABCB", the function should return false.

## Approach
The algorithm uses depth-first search to explore all possible paths in the grid. It checks each cell in the grid to see if it matches the first letter of the word, and then recursively checks adjacent cells for subsequent letters. The function returns true as soon as it finds a path that matches the entire word.

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
        
        // Define the directions for adjacent cells
        vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        // Function to perform depth-first search
        function<bool(int, int, int)> dfs = [&](int x, int y, int index) {
            // If the current character does not match, return false
            if (board[x][y] != word[index]) return false;
            
            // If the entire word has been found, return true
            if (index == word.size() - 1) return true;
            
            // Mark the current cell as visited
            char temp = board[x][y];
            board[x][y] = '#';
            
            // Recursively check adjacent cells
            for (auto& dir : directions) {
                int nx = x + dir.first;
                int ny = y + dir.second;
                if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && dfs(nx, ny, index + 1)) {
                    return true;
                }
            }
            
            // Unmark the current cell
            board[x][y] = temp;
            return false;
        };
        
        // Check each cell in the grid
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
Input: board = [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], word = "ABCCED"
Output: true
Input: board = [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], word = "SEE"
Output: true
Input: board = [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], word = "ABCB"
Output: false
```

## Key Takeaways
- Use depth-first search to explore all possible paths in the grid.
- Mark visited cells to avoid revisiting them and to ensure that each cell is used only once.
- Recursively check adjacent cells for subsequent letters in the word.