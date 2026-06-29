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
and word `ABCCED`, the output should be `true` because the word can be found in the grid.

## Approach
The algorithm uses depth-first search (DFS) to explore all possible paths from each cell. It checks if the current character in the word matches the character in the current cell, and if so, continues the search from the adjacent cells.

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
        int rows = board.size();
        int cols = board[0].size();
        
        // define the possible directions for adjacent cells
        vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        // function to perform DFS
        function<bool(int, int, int)> dfs = [&](int x, int y, int index) {
            // if the current character does not match, return false
            if (board[x][y] != word[index]) return false;
            
            // if the entire word is found, return true
            if (index == word.size() - 1) return true;
            
            // mark the current cell as visited
            char temp = board[x][y];
            board[x][y] = '#';
            
            // explore all adjacent cells
            for (auto& dir : directions) {
                int nx = x + dir.first;
                int ny = y + dir.second;
                
                // if the adjacent cell is within bounds and not visited
                if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && board[nx][ny] != '#') {
                    // continue the search from the adjacent cell
                    if (dfs(nx, ny, index + 1)) return true;
                }
            }
            
            // unmark the current cell
            board[x][y] = temp;
            
            // if no path is found, return false
            return false;
        };
        
        // search from each cell in the board
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (dfs(i, j, 0)) return true;
            }
        }
        
        // if no path is found from any cell, return false
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
- The algorithm uses DFS to explore all possible paths from each cell.
- The time complexity is exponential due to the recursive nature of DFS, but it is necessary to explore all possible paths.
- The space complexity is linear due to the recursive call stack and the visited set.