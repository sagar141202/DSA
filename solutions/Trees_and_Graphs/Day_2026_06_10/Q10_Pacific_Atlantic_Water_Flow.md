# Pacific Atlantic Water Flow

## Problem Statement
There is a matrix of m x n cells, each cell has a certain height. Water can flow from a cell to its adjacent cells (up, down, left, right) if the adjacent cell has a higher or equal height. There are two oceans: Pacific and Atlantic. The Pacific ocean is located on the left and top edges of the matrix, while the Atlantic ocean is located on the right and bottom edges. We need to find all the cells from which water can flow to both oceans.

## Approach
The algorithm uses depth-first search (DFS) to traverse the cells that can flow to the Pacific and Atlantic oceans. We start from the edges of the matrix and mark all the cells that can flow to each ocean. Then, we find the intersection of the two sets of cells.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

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
        
        // DFS from Pacific
        for (int i = 0; i < m; i++) {
            dfs(matrix, pacific, i, 0);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, pacific, 0, j);
        }
        
        // DFS from Atlantic
        for (int i = 0; i < m; i++) {
            dfs(matrix, atlantic, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            dfs(matrix, atlantic, m - 1, j);
        }
        
        // Find intersection
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
        
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (auto& dir : directions) {
            int x = i + dir.first;
            int y = j + dir.second;
            if (x >= 0 && x < matrix.size() && y >= 0 && y < matrix[0].size() && matrix[x][y] >= matrix[i][j]) {
                dfs(matrix, visited, x, y);
            }
        }
    }
};

```

## Test Cases
```
Input: [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

## Key Takeaways
- Use DFS to traverse the cells that can flow to the Pacific and Atlantic oceans.
- Start from the edges of the matrix and mark all the cells that can flow to each ocean.
- Find the intersection of the two sets of cells to get the final result.
- The time complexity is O(m * n) and the space complexity is O(m * n).