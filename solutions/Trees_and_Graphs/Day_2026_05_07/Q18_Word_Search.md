# Word Search

## Problem Statement
Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once. For example, given the following board and word:
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
and word = "ABCCED", return true. The word can be constructed from letters of sequentially adjacent cell.

## Approach
The solution involves using a Depth-First Search (DFS) algorithm to traverse the grid and check if the word exists. We start at each cell and explore all possible paths. If we find a path that matches the word, we return true.

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
        // Get the number of rows and columns
        int rows = board.size();
        int cols = board[0].size();
        
        // Define the directions for DFS
        vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        // Function to perform DFS
        function<bool(int, int, int)> dfs = [&](int x, int y, int index) {
            // If the current character does not match, return false
            if (board[x][y] != word[index]) return false;
            
            // If we have found the entire word, return true
            if (index == word.size() - 1) return true;
            
            // Mark the current cell as visited
            char temp = board[x][y];
            board[x][y] = '#';
            
            // Perform DFS in all directions
            for (auto& dir : directions) {
                int nx = x + dir.first;
                int ny = y + dir.second;
                
                // Check if the new position is valid
                if (nx >= 0 && nx < rows && ny >= 0 && ny < cols) {
                    if (dfs(nx, ny, index + 1)) return true;
                }
            }
            
            // Unmark the current cell
            board[x][y] = temp;
            
            // If no path is found, return false
            return false;
        };
        
        // Perform DFS from each cell
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
Input: 
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
Output: true

Input: 
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "SEE"
Output: true

Input: 
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCB"
Output: false
```

## Key Takeaways
- Use DFS to traverse the grid and check if the word exists.
- Mark the current cell as visited to avoid revisiting it.
- Unmark the current cell after exploring all possible paths.
- Perform DFS from each cell to cover all possible starting positions.