# Word Search

## Problem Statement
Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once. For example, given a board like this:
```
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
```
and a word like "ABCCED", the function returns true because the word can be found in the grid. However, if the word is "SEE", the function returns true, but if the word is "ABCB", the function returns false.

## Approach
The algorithm uses a Depth-First Search (DFS) approach to traverse the grid and check for the word. It iterates over each cell in the grid and checks if the current character matches the first character of the word. If it does, it calls the DFS function to check the rest of the word.

## Complexity
- Time: O(N * M * 4^L)
- Space: O(L)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int rows = board.size();
        int cols = board[0].size();
        
        // Iterate over each cell in the grid
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // Check if the current character matches the first character of the word
                if (board[i][j] == word[0]) {
                    // Call the DFS function to check the rest of the word
                    if (dfs(board, word, i, j, 0)) {
                        return true;
                    }
                }
            }
        }
        
        return false;
    }
    
    bool dfs(vector<vector<char>>& board, string word, int i, int j, int k) {
        int rows = board.size();
        int cols = board[0].size();
        
        // If the current character does not match the character in the word, return false
        if (board[i][j] != word[k]) {
            return false;
        }
        
        // If the entire word has been found, return true
        if (k == word.size() - 1) {
            return true;
        }
        
        // Mark the current cell as visited
        char temp = board[i][j];
        board[i][j] = '#';
        
        // Check the adjacent cells
        int directions[][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (int dir = 0; dir < 4; dir++) {
            int ni = i + directions[dir][0];
            int nj = j + directions[dir][1];
            
            // Check if the adjacent cell is within the grid and has not been visited
            if (ni >= 0 && ni < rows && nj >= 0 && nj < cols && board[ni][nj] != '#') {
                // Recursively call the DFS function on the adjacent cell
                if (dfs(board, word, ni, nj, k + 1)) {
                    return true;
                }
            }
        }
        
        // Unmark the current cell as visited
        board[i][j] = temp;
        
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
- Use a DFS approach to traverse the grid and check for the word.
- Mark the current cell as visited to avoid revisiting it.
- Unmark the current cell as visited after checking all its adjacent cells.