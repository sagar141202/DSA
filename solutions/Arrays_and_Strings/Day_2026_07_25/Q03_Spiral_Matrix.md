# Spiral Matrix

## Problem Statement
Given a matrix of size m x n, fill it with numbers from 1 to m*n in a spiral order, starting from the top-left corner and moving clockwise. The matrix is filled in the following order: from left to right, then from top to bottom, then from right to left, and finally from bottom to top. For example, given a 3x3 matrix, the spiral order is: 
[
  [1, 2, 3],
  [8, 9, 4],
  [7, 6, 5]
]

## Approach
The algorithm uses four pointers (top, bottom, left, right) to represent the current boundaries of the matrix. It fills the matrix in a spiral order by iterating over the elements in the following order: from left to right, then from top to bottom, then from right to left, and finally from bottom to top.

## Complexity
- Time: O(m*n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> generateMatrix(int n) {
        std::vector<std::vector<int>> matrix(n, std::vector<int>(n, 0));
        int top = 0, bottom = n - 1, left = 0, right = n - 1;
        int num = 1;
        
        while (top <= bottom && left <= right) {
            // Fill from left to right
            for (int i = left; i <= right; i++) {
                matrix[top][i] = num++;
            }
            top++;
            
            // Fill from top to bottom
            for (int i = top; i <= bottom; i++) {
                matrix[i][right] = num++;
            }
            right--;
            
            // Fill from right to left
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    matrix[bottom][i] = num++;
                }
                bottom--;
            }
            
            // Fill from bottom to top
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    matrix[i][left] = num++;
                }
                left++;
            }
        }
        
        return matrix;
    }
};
```

## Test Cases
```
Input: n = 3
Output: 
[
  [1, 2, 3],
  [8, 9, 4],
  [7, 6, 5]
]

Input: n = 4
Output: 
[
  [1, 2, 3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10, 9, 8, 7]
]
```

## Key Takeaways
- Use four pointers (top, bottom, left, right) to represent the current boundaries of the matrix.
- Fill the matrix in a spiral order by iterating over the elements in the following order: from left to right, then from top to bottom, then from right to left, and finally from bottom to top.
- The time complexity is O(m*n) and the space complexity is O(1), excluding the space required for the output matrix.