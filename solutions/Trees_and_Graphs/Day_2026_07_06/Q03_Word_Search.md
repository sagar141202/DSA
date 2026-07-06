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
and a word like "ABCCED", the function returns true because the word can be found in the grid. However, for a word like "SEE", the function returns true, and for a word like "ABCB", it returns false.

## Approach
We will use a Depth-First Search (DFS) approach to solve this problem, checking all possible paths from each cell in the grid. The algorithm will explore all adjacent cells and backtrack when a dead end is reached. We will also keep track of visited cells to avoid revisiting them.

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
        // Get the dimensions of the board
        int rows = board.size();
        int cols = board[0].size();

        // Define the possible directions for DFS
        vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        // Function to perform DFS
        function<bool(int, int, int)> dfs = [&](int row, int col, int index) {
            // If the current character does not match, return false
            if (board[row][col] != word[index]) return false;

            // If we have reached the end of the word, return true
            if (index == word.size() - 1) return true;

            // Mark the current cell as visited
            char temp = board[row][col];
            board[row][col] = '#';

            // Explore all adjacent cells
            for (auto& dir : directions) {
                int newRow = row + dir.first;
                int newCol = col + dir.second;

                // Check if the new cell is within the board boundaries
                if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols) {
                    // If the DFS from the new cell returns true, return true
                    if (dfs(newRow, newCol, index + 1)) return true;
                }
            }

            // If no path is found, backtrack and unmark the current cell
            board[row][col] = temp;
            return false;
        };

        // Perform DFS from each cell in the board
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (dfs(i, j, 0)) return true;
            }
        }

        // If no path is found from any cell, return false
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
- The problem can be solved using a Depth-First Search (DFS) approach.
- We need to keep track of visited cells to avoid revisiting them.
- The time complexity is O(N * M * 4^L), where N and M are the dimensions of the board and L is the length of the word.