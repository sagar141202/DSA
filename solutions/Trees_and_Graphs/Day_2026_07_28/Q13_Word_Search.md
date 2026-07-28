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
and word = "ABCCED", the function returns true because the word can be found in the grid. However, if the word is "SEE", the function returns true, but if the word is "ABCB", the function returns false.

## Approach
The approach is to use a depth-first search (DFS) algorithm to explore all possible paths in the grid. We start from each cell in the grid and try to match the word. If a match is found, we return true. The algorithm checks all eight possible directions (up, down, left, right, and four diagonals are not considered as the problem statement only considers horizontal and vertical directions) from each cell.

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
        // Get the dimensions of the board
        int rows = board.size();
        int cols = board[0].size();
        
        // Define the possible directions
        vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        // Function to perform DFS
        bool dfs(int i, int j, int index) {
            // If the index is equal to the length of the word, we have found the word
            if (index == word.size()) return true;
            
            // If the current cell is out of bounds or the character does not match, return false
            if (i < 0 || i >= rows || j < 0 || j >= cols || board[i][j] != word[index]) return false;
            
            // Mark the current cell as visited
            char temp = board[i][j];
            board[i][j] = '#';
            
            // Perform DFS in all four directions
            for (auto& dir : directions) {
                if (dfs(i + dir.first, j + dir.second, index + 1)) return true;
            }
            
            // Backtrack
            board[i][j] = temp;
            return false;
        }
        
        // Perform DFS from each cell
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (dfs(i, j, 0)) return true;
            }
        }
        
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
- The problem can be solved using a depth-first search (DFS) algorithm.
- We need to perform DFS from each cell in the grid to find the word.
- We need to mark the current cell as visited to avoid revisiting it and to backtrack after exploring all possible paths.