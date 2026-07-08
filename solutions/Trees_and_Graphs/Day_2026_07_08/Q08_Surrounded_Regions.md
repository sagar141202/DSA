# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. A region is captured by flipping all 'O's in that region to 'X'. The region is surrounded if all 'O' nodes on the border of the region are connected to the border of the board. The problem can be solved by first identifying all 'O' regions connected to the border and then flipping all other 'O' regions to 'X'. The board size is up to 200x200, and the input is a 2D vector of characters.

## Approach
The algorithm uses depth-first search (DFS) to mark all 'O' regions connected to the border. Then, it iterates over the board to flip all unmarked 'O' regions to 'X' and all marked 'O' regions back to 'O'.

## Complexity
- Time: O(M*N)
- Space: O(M*N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void solve(vector<vector<char>>& board) {
        if (board.empty()) return;
        
        int m = board.size();
        int n = board[0].size();
        
        // Mark all 'O' regions connected to the border
        for (int i = 0; i < m; i++) {
            dfs(board, i, 0);
            dfs(board, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            dfs(board, 0, j);
            dfs(board, m - 1, j);
        }
        
        // Flip all unmarked 'O' regions to 'X' and all marked 'O' regions back to 'O'
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') board[i][j] = 'X';
                else if (board[i][j] == '#') board[i][j] = 'O';
            }
        }
    }
    
    void dfs(vector<vector<char>>& board, int i, int j) {
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] != 'O') return;
        board[i][j] = '#';
        dfs(board, i - 1, j);
        dfs(board, i + 1, j);
        dfs(board, i, j - 1);
        dfs(board, i, j + 1);
    }
};

```

## Test Cases
```
Input: 
X X X X
X O O X
X X O X
X O X X

Output: 
X X X X
X X X X
X X X X
X O X X
```

## Key Takeaways
- Identify all 'O' regions connected to the border using DFS.
- Mark these regions with a temporary character to distinguish them from other 'O' regions.
- Flip all unmarked 'O' regions to 'X' and all marked 'O' regions back to 'O' to get the final result.