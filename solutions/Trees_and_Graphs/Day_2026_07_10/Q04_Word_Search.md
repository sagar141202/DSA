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
and the word "ABCCED", the function should return `true` because the word can be found in the grid.

## Approach
The algorithm uses a depth-first search (DFS) approach to explore all possible paths in the grid. It starts from each cell in the grid and checks if the current cell matches the first character of the word. If it does, it recursively checks the neighboring cells to see if the rest of the word can be formed.

## Complexity
- Time: O(N * M * 4^L)
- Space: O(N * M + L)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        if (word.empty()) return true;
        if (board.empty() || board[0].empty()) return false;
        
        int rows = board.size();
        int cols = board[0].size();
        
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] == word[0]) {
                    if (dfs(board, word, i, j, 0, visited)) return true;
                }
            }
        }
        
        return false;
    }
    
    bool dfs(vector<vector<char>>& board, string& word, int i, int j, int k, vector<vector<bool>>& visited) {
        if (k == word.size()) return true;
        
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || visited[i][j] || board[i][j] != word[k]) {
            return false;
        }
        
        visited[i][j] = true;
        
        bool found = dfs(board, word, i + 1, j, k + 1, visited) ||
                       dfs(board, word, i - 1, j, k + 1, visited) ||
                       dfs(board, word, i, j + 1, k + 1, visited) ||
                       dfs(board, word, i, j - 1, k + 1, visited);
        
        visited[i][j] = false;
        
        return found;
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
- Use a visited matrix to keep track of visited cells and avoid revisiting them.
- The time complexity is exponential due to the recursive nature of DFS, but it is necessary to explore all possible paths.