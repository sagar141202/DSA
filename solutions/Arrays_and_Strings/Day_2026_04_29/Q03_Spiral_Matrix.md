# Spiral Matrix

## Problem Statement
Given a matrix of size m x n, write a function that generates a spiral matrix. The function should take an integer m (number of rows) and an integer n (number of columns) as input, and return a 2D vector representing the spiral matrix. The spiral matrix should be filled with numbers from 1 to m*n in a spiral order, starting from the top left corner and moving clockwise. For example, given m = 3 and n = 3, the output should be [[1, 2, 3], [8, 9, 4], [7, 6, 5]]. The input constraints are 1 <= m <= 10^3 and 1 <= n <= 10^3.

## Approach
The algorithm uses four pointers (top, bottom, left, right) to keep track of the current boundaries of the matrix. It fills the matrix in a spiral order by iterating over the elements in a clockwise direction. The algorithm continues until all elements are filled.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> generateMatrix(int m, int n) {
        std::vector<std::vector<int>> matrix(m, std::vector<int>(n, 0));
        int top = 0, bottom = m - 1, left = 0, right = n - 1;
        int num = 1;
        
        while (top <= bottom && left <= right) {
            // fill the top row from left to right
            for (int i = left; i <= right; i++) {
                matrix[top][i] = num++;
            }
            top++;
            
            // fill the right column from top to bottom
            for (int i = top; i <= bottom; i++) {
                matrix[i][right] = num++;
            }
            right--;
            
            // fill the bottom row from right to left
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    matrix[bottom][i] = num++;
                }
                bottom--;
            }
            
            // fill the left column from bottom to top
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
Input: m = 3, n = 3
Output: [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

Input: m = 4, n = 4
Output: [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
```

## Key Takeaways
- Use four pointers to keep track of the current boundaries of the matrix.
- Fill the matrix in a spiral order by iterating over the elements in a clockwise direction.
- Continue the algorithm until all elements are filled.