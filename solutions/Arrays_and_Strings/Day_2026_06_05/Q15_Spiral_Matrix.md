# Spiral Matrix

## Problem Statement
Given a matrix of size m x n, generate a spiral matrix where the elements are filled in a spiral order, starting from the top left and moving clockwise. The matrix is filled with numbers from 1 to m*n in ascending order. For example, given a 3x3 matrix, the spiral matrix would be:
```
1 2 3
8 9 4
7 6 5
```
The constraints are 1 <= m, n <= 20 and -100 <= matrix[i][j] <= 100.

## Approach
The algorithm uses four pointers to keep track of the current boundaries of the matrix. It fills the matrix in a spiral order by iterating over the elements in a clockwise direction. The intuition is to start from the outermost layer and move inwards, filling the elements in a spiral pattern.

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
        int count = 1;
        int top = 0, bottom = n - 1, left = 0, right = n - 1;
        
        while (top <= bottom && left <= right) {
            // fill the top row from left to right
            for (int i = left; i <= right; i++) {
                matrix[top][i] = count++;
            }
            top++;
            
            // fill the right column from top to bottom
            for (int i = top; i <= bottom; i++) {
                matrix[i][right] = count++;
            }
            right--;
            
            // fill the bottom row from right to left
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    matrix[bottom][i] = count++;
                }
                bottom--;
            }
            
            // fill the left column from bottom to top
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    matrix[i][left] = count++;
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
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
```

## Key Takeaways
- Initialize four pointers (top, bottom, left, right) to keep track of the current boundaries of the matrix.
- Fill the matrix in a spiral order by iterating over the elements in a clockwise direction.
- Use a counter to keep track of the current number to be filled in the matrix.