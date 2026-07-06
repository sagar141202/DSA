# Pacific Atlantic Water Flow

## Problem Statement
Given an m x n matrix of non-negative integers representing the height of each cell in a continent, the Pacific ocean touches the left and top edges, and the Atlantic ocean touches the right and bottom edges. Water can flow from a cell to its four neighboring cells if the neighboring cell's height is not less than the current cell's height. Determine which cells can flow to both the Pacific and Atlantic oceans. The input matrix will be in the range of [1, 200] for both m and n, and the values in the matrix will be in the range [0, 10^5]. For example, given the following matrix:
```
[1,2,2,3,5]
[3,2,3,4,4]
[2,4,5,3,1]
[6,7,1,4,5]
[5,1,1,2,4]
```
The cells that can flow to both the Pacific and Atlantic oceans are `[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]`.

## Approach
The algorithm uses Depth-First Search (DFS) to traverse the matrix from both the Pacific and Atlantic coastlines, marking the cells that can flow to each ocean. Then, it finds the intersection of the two sets of marked cells. This approach ensures that only cells that can flow to both oceans are included in the result.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return {};
        
        int m = matrix.size();
        int n = matrix[0].size();
        
        vector<vector<bool>> pacific(m, vector<bool>(n, false));
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));
        
        // DFS from Pacific coastline
        for (int i = 0; i < m; i++) {
            dfs(matrix, pacific, i, 0);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, pacific, 0, j);
        }
        
        // DFS from Atlantic coastline
        for (int i = 0; i < m; i++) {
            dfs(matrix, atlantic, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, atlantic, m - 1, j);
        }
        
        // Find intersection of Pacific and Atlantic cells
        vector<vector<int>> result;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    result.push_back({i, j});
                }
            }
        }
        return result;
    }
    
    void dfs(vector<vector<int>>& matrix, vector<vector<bool>>& visited, int i, int j) {
        if (visited[i][j]) return;
        visited[i][j] = true;
        
        int m = matrix.size();
        int n = matrix[0].size();
        
        // Explore neighboring cells
        if (i > 0 && matrix[i - 1][j] >= matrix[i][j]) {
            dfs(matrix, visited, i - 1, j);
        }
        if (i < m - 1 && matrix[i + 1][j] >= matrix[i][j]) {
            dfs(matrix, visited, i + 1, j);
        }
        if (j > 0 && matrix[i][j - 1] >= matrix[i][j]) {
            dfs(matrix, visited, i, j - 1);
        }
        if (j < n - 1 && matrix[i][j + 1] >= matrix[i][j]) {
            dfs(matrix, visited, i, j + 1);
        }
    }
};

```

## Test Cases
```
Input: 
[
 [1,2,2,3,5],
 [3,2,3,4,4],
 [2,4,5,3,1],
 [6,7,1,4,5],
 [5,1,1,2,4]
]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

## Key Takeaways
- Use DFS to traverse the matrix from both coastlines.
- Mark cells that can flow to each ocean using separate visited matrices.
- Find the intersection of the two sets of marked cells to determine which cells can flow to both oceans.
- The algorithm has a time complexity of O(m*n) and a space complexity of O(m*n), where m and n are the dimensions of the input matrix.