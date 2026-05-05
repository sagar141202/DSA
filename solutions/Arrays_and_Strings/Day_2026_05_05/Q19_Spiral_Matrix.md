# Spiral Matrix

## Problem Statement
Given a matrix of size m x n, write a function that traverses the matrix in a spiral order and returns the elements in the order they were visited. The function should take two integers m and n as input, representing the number of rows and columns in the matrix, and return a vector of integers representing the spiral order of the matrix elements. For example, given the following 3x3 matrix:
```
1 2 3
4 5 6
7 8 9
```
The function should return the vector:
```
1 2 3 6 9 8 7 4 5
```
The constraints are 1 <= m, n <= 10, and -100 <= matrix[i][j] <= 100.

## Approach
The algorithm uses four pointers (top, bottom, left, right) to represent the current boundaries of the matrix. It iterates through the matrix in a spiral order by moving the pointers inward after each iteration. The spiral order is achieved by alternating between moving right, down, left, and up.

## Complexity
- Time: O(m*n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>

class Solution {
public:
    std::vector<int> spiralOrder(std::vector<std::vector<int>>& matrix) {
        std::vector<int> result;
        if (matrix.empty()) return result;
        
        int top = 0;
        int bottom = matrix.size() - 1;
        int left = 0;
        int right = matrix[0].size() - 1;
        
        while (top <= bottom && left <= right) {
            // Move right
            for (int i = left; i <= right; i++) {
                result.push_back(matrix[top][i]);
            }
            top++;
            
            // Move down
            for (int i = top; i <= bottom; i++) {
                result.push_back(matrix[i][right]);
            }
            right--;
            
            // Move left
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    result.push_back(matrix[bottom][i]);
                }
                bottom--;
            }
            
            // Move up
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    result.push_back(matrix[i][left]);
                }
                left++;
            }
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## Key Takeaways
- Use four pointers to represent the current boundaries of the matrix.
- Alternate between moving right, down, left, and up to achieve the spiral order.
- Be careful when handling edge cases, such as when the matrix has an odd number of rows or columns.