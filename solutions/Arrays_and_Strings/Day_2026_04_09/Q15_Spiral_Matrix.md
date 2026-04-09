# Spiral Matrix

## Problem Statement
Given a matrix of size m x n, write a function that traverses the matrix in a spiral order and returns the elements in the order they were visited. The spiral order starts from the top left corner and moves clockwise. For example, given the following matrix:
```
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
```
The output should be: `[1, 2, 3, 6, 9, 8, 7, 4, 5]`.

## Approach
The algorithm uses four pointers to keep track of the current boundaries of the matrix. It iterates through the elements in a spiral order by moving the pointers accordingly. The spiral order is achieved by first traversing the top row, then the right column, then the bottom row, and finally the left column.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <vector>

class Solution {
public:
    std::vector<int> spiralOrder(std::vector<std::vector<int>>& matrix) {
        std::vector<int> result;
        if (matrix.empty()) return result;
        
        int rowBegin = 0;
        int rowEnd = matrix.size() - 1;
        int colBegin = 0;
        int colEnd = matrix[0].size() - 1;
        
        while (rowBegin <= rowEnd && colBegin <= colEnd) {
            // Traverse from left to right
            for (int i = colBegin; i <= colEnd; ++i) {
                result.push_back(matrix[rowBegin][i]);
            }
            rowBegin++;
            
            // Traverse from top to bottom
            for (int i = rowBegin; i <= rowEnd; ++i) {
                result.push_back(matrix[i][colEnd]);
            }
            colEnd--;
            
            // Traverse from right to left
            if (rowBegin <= rowEnd) {
                for (int i = colEnd; i >= colBegin; --i) {
                    result.push_back(matrix[rowEnd][i]);
                }
            }
            rowEnd--;
            
            // Traverse from bottom to top
            if (colBegin <= colEnd) {
                for (int i = rowEnd; i >= rowBegin; --i) {
                    result.push_back(matrix[i][colBegin]);
                }
            }
            colBegin++;
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
```

## Key Takeaways
- Initialize four pointers to keep track of the current boundaries of the matrix.
- Traverse the elements in a spiral order by moving the pointers accordingly.
- Use conditional statements to handle edge cases where the matrix has an odd number of rows or columns.