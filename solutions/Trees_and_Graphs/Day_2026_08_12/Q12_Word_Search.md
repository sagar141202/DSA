# Word Search

## Problem Statement
Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once. For example, given a 2D board containing the letters `[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]` and the word `"ABCCED"`, the output should be `true` because the word can be found in the grid.

## Approach
The algorithm uses depth-first search (DFS) to traverse the grid and check if the word can be formed. It iterates over each cell in the grid and calls the DFS function to check if the word can be formed starting from that cell. The DFS function checks if the current character in the word matches the character in the current cell, and if so, it recursively calls itself for the adjacent cells.

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
        int rows = board.size();
        int cols = board[0].size();
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] == word[0]) {
                    if (dfs(board, word, i, j, 0)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
    
    bool dfs(vector<vector<char>>& board, string word, int i, int j, int k) {
        if (k == word.size()) {
            return true;
        }
        
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || word[k] != board[i][j]) {
            return false;
        }
        
        char temp = board[i][j];
        board[i][j] = '#';
        
        bool found = dfs(board, word, i + 1, j, k + 1) ||
                      dfs(board, word, i - 1, j, k + 1) ||
                      dfs(board, word, i, j + 1, k + 1) ||
                      dfs(board, word, i, j - 1, k + 1);
        
        board[i][j] = temp;
        
        return found;
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
- The DFS approach is suitable for this problem because it allows us to explore all possible paths in the grid.
- We need to mark the visited cells to avoid revisiting them and to ensure that the same letter cell is not used more than once.
- The time complexity is exponential due to the recursive nature of the DFS approach.