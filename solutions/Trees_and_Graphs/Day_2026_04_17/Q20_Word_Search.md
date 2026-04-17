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
and the word "ABCCED", the function returns true, because the word can be found in the grid. However, given the word "SEE", the function returns true, and given the word "ABCB", the function returns false.

## Approach
The algorithm uses a depth-first search (DFS) approach to explore all possible paths in the grid. It starts from each cell and checks if the current character matches the first character of the word. If it does, it recursively checks the adjacent cells for the remaining characters of the word.

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
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                if (dfs(board, word, i, j, 0)) return true;
            }
        }
        return false;
    }
    
    bool dfs(vector<vector<char>>& board, string word, int i, int j, int k) {
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || word[k] != board[i][j]) {
            return false;
        }
        if (k == word.size() - 1) return true;
        
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
- Mark visited cells to avoid revisiting them.
- Restore the original state of the grid after exploring each path.