# Spiral Matrix

## Problem Statement
Given an m x n matrix, return all elements of the matrix in spiral order. The spiral order starts from the top left, goes to the right, then goes down, then to the left, and finally goes up. The constraints are 1 <= m <= 10, m <= rows <= 10^3, 1 <= n <= 10, n <= columns <= 10^3, and -100 <= matrix[i][j] <= 100. For example, given the matrix [[1,2,3],[4,5,6],[7,8,9]], the output should be [1,2,3,6,9,8,7,4,5].

## Approach
The algorithm uses four pointers to track the current boundaries of the matrix. It iterates through the matrix in a spiral order by moving the pointers accordingly. The intuition is to start from the outermost layer and move inwards.

## Complexity
- Time: O(m*n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> result;
        if (matrix.empty() || matrix[0].empty()) return result;
        
        int rowStart = 0, rowEnd = matrix.size() - 1;
        int colStart = 0, colEnd = matrix[0].size() - 1;
        
        while (rowStart <= rowEnd && colStart <= colEnd) {
            // Traverse from left to right
            for (int i = colStart; i <= colEnd; i++) {
                result.push_back(matrix[rowStart][i]);
            }
            rowStart++;
            
            // Traverse from top to bottom
            for (int i = rowStart; i <= rowEnd; i++) {
                result.push_back(matrix[i][colEnd]);
            }
            colEnd--;
            
            // Traverse from right to left
            if (rowStart <= rowEnd) {
                for (int i = colEnd; i >= colStart; i--) {
                    result.push_back(matrix[rowEnd][i]);
                }
                rowEnd--;
            }
            
            // Traverse from bottom to top
            if (colStart <= colEnd) {
                for (int i = rowEnd; i >= rowStart; i--) {
                    result.push_back(matrix[i][colStart]);
                }
                colStart++;
            }
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Input: [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## Key Takeaways
- Initialize four pointers to track the current boundaries of the matrix.
- Traverse the matrix in a spiral order by moving the pointers accordingly.
- Handle edge cases where the matrix is empty or has only one row/column.