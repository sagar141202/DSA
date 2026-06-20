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
and word = "ABCCED", the function returns true, because the word can be found in the grid. However, given the word = "SEE", the function returns true, and given the word = "ABCB", the function returns false.

## Approach
We use depth-first search to traverse the grid and find the word. We start from each cell and explore all possible paths. If we find a path that matches the word, we return true. We use a visited set to keep track of visited cells and avoid revisiting them.

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
        
        // Define the directions for DFS
        vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        // Perform DFS from each cell
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] == word[0]) {
                    // Use a visited set to keep track of visited cells
                    vector<vector<bool>> visited(rows, vector<bool>(cols, false));
                    if (dfs(board, word, i, j, 0, directions, visited)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
    
    bool dfs(vector<vector<char>>& board, string word, int i, int j, int index, vector<pair<int, int>>& directions, vector<vector<bool>>& visited) {
        // If we have found the entire word, return true
        if (index == word.size()) {
            return true;
        }
        
        // If the current cell is out of bounds or the character does not match, return false
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || visited[i][j] || board[i][j] != word[index]) {
            return false;
        }
        
        // Mark the current cell as visited
        visited[i][j] = true;
        
        // Perform DFS in all directions
        for (auto& direction : directions) {
            if (dfs(board, word, i + direction.first, j + direction.second, index + 1, directions, visited)) {
                return true;
            }
        }
        
        // Unmark the current cell as visited
        visited[i][j] = false;
        
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
- Use depth-first search to traverse the grid and find the word.
- Use a visited set to keep track of visited cells and avoid revisiting them.
- Perform DFS in all directions from each cell to find the word.