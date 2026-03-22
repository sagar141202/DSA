# Spiral Matrix

## Problem Statement
Given a matrix of size m x n, write a function that fills the matrix with numbers from 1 to m*n in a spiral order, starting from the top left and moving clockwise. The function should take two integers m and n as input and return a 2D vector representing the filled matrix. For example, given m = 3 and n = 3, the function should return:
```
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
```
Constraints: 1 <= m <= 100, 1 <= n <= 100.

## Approach
The algorithm uses four pointers to keep track of the current boundaries of the matrix. It starts by filling the top row, then the right column, the bottom row, and the left column, and repeats this process until all numbers are filled. The direction of filling is determined by the current position of the pointers.

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
        int count = 1;
        int top = 0;
        int bottom = m - 1;
        int left = 0;
        int right = n - 1;
        
        while (top <= bottom && left <= right) {
            // Fill the top row
            for (int i = left; i <= right; i++) {
                matrix[top][i] = count++;
            }
            top++;
            
            // Fill the right column
            for (int i = top; i <= bottom; i++) {
                matrix[i][right] = count++;
            }
            right--;
            
            // Fill the bottom row
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    matrix[bottom][i] = count++;
                }
                bottom--;
            }
            
            // Fill the left column
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
Input: m = 3, n = 3
Output: 
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
Input: m = 4, n = 4
Output: 
[
 [ 1, 2, 3, 4 ],
 [12,13,14, 5 ],
 [11,16,15, 6 ],
 [10, 9, 8, 7 ]
]
```

## Key Takeaways
- Initialize four pointers (top, bottom, left, right) to keep track of the current boundaries of the matrix.
- Fill the matrix in a spiral order by iterating over the top row, right column, bottom row, and left column, and update the pointers accordingly.
- Use a counter variable to keep track of the current number to be filled in the matrix.