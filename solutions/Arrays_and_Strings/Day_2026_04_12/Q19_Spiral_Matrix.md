# Spiral Matrix

## Problem Statement
Given a matrix of size m x n, write a function that traverses the matrix in a spiral order (clockwise) and returns the elements in the order they were visited. The matrix is filled with distinct integers. For example, given the following matrix:
```
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
```
The output should be: `[1, 2, 3, 6, 9, 8, 7, 4, 5]`. The function should handle matrices of different sizes and should be efficient in terms of time and space complexity.

## Approach
The algorithm uses four pointers (top, bottom, left, right) to keep track of the current boundaries of the matrix. It then iterates over the elements in a spiral order by moving the pointers accordingly. The spiral order is achieved by first traversing the top row from left to right, then the right column from top to bottom, then the bottom row from right to left, and finally the left column from bottom to top.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <vector>

class Solution {
public:
    std::vector<int> spiralOrder(std::vector<std::vector<int>>& matrix) {
        if (matrix.empty()) return {};
        
        int top = 0;
        int bottom = matrix.size() - 1;
        int left = 0;
        int right = matrix[0].size() - 1;
        
        std::vector<int> result;
        
        while (top <= bottom && left <= right) {
            // Traverse from left to right
            for (int i = left; i <= right; i++) {
                result.push_back(matrix[top][i]);
            }
            top++;
            
            // Traverse from top to bottom
            for (int i = top; i <= bottom; i++) {
                result.push_back(matrix[i][right]);
            }
            right--;
            
            // Traverse from right to left
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    result.push_back(matrix[bottom][i]);
                }
                bottom--;
            }
            
            // Traverse from bottom to top
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
Input: 
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

Input: 
[
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12]
]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
```

## Key Takeaways
- The spiral order traversal can be achieved by maintaining four pointers (top, bottom, left, right) to keep track of the current boundaries of the matrix.
- The time complexity of the solution is O(m * n), where m and n are the number of rows and columns in the matrix respectively.
- The space complexity of the solution is O(m * n), which is used to store the result.