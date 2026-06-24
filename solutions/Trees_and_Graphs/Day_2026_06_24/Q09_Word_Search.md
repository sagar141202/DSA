# Word Search

## Problem Statement
Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

## Approach
We will use a Depth-First Search (DFS) approach to traverse the grid and check if the word exists. We will start from each cell in the grid and explore all possible paths. The algorithm will return true if the word is found, and false otherwise.

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
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] == word[0]) {
                    if (dfs(board, word, i, j, 0, visited)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    bool dfs(vector<vector<char>>& board, string word, int i, int j, int k, vector<vector<bool>>& visited) {
        if (k == word.size()) {
            return true;
        }

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
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
], word = "ABCCED"
Output: true

Input: board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
], word = "SEE"
Output: true

Input: board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
], word = "ABCB"
Output: false
```

## Key Takeaways
- Use DFS to traverse the grid and explore all possible paths.
- Keep track of visited cells to avoid revisiting the same cell.
- Use a recursive function to simplify the code and improve readability.