# Spiral Matrix

## Problem Statement
Given an integer `n`, generate a spiral matrix of size `n x n` filled with numbers from 1 to `n * n` in a spiral pattern, starting from the top left and moving clockwise. The matrix should be filled in the following order: top row from left to right, right column from top to bottom, bottom row from right to left, and left column from bottom to top. For example, given `n = 3`, the output should be:
```
[[1, 2, 3],
 [8, 9, 4],
 [7, 6, 5]]
```
Constraints: `1 <= n <= 20`

## Approach
The algorithm uses four pointers (top, bottom, left, right) to keep track of the current boundaries of the matrix. It fills the matrix in a spiral pattern by iterating over the elements in a clockwise direction. The algorithm continues until all elements are filled.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<vector<int>> generateMatrix(int n) {
    vector<vector<int>> matrix(n, vector<int>(n, 0));
    int top = 0, bottom = n - 1, left = 0, right = n - 1;
    int num = 1;
    
    while (top <= bottom && left <= right) {
        // Fill top row from left to right
        for (int i = left; i <= right; i++) {
            matrix[top][i] = num++;
        }
        top++;
        
        // Fill right column from top to bottom
        for (int i = top; i <= bottom; i++) {
            matrix[i][right] = num++;
        }
        right--;
        
        // Fill bottom row from right to left
        if (top <= bottom) {
            for (int i = right; i >= left; i--) {
                matrix[bottom][i] = num++;
            }
            bottom--;
        }
        
        // Fill left column from bottom to top
        if (left <= right) {
            for (int i = bottom; i >= top; i--) {
                matrix[i][left] = num++;
            }
            left++;
        }
    }
    
    return matrix;
}
```

## Test Cases
```
Input: n = 3
Output: [[1, 2, 3],
          [8, 9, 4],
          [7, 6, 5]]

Input: n = 4
Output: [[1, 2, 3, 4],
          [12, 13, 14, 5],
          [11, 16, 15, 6],
          [10, 9, 8, 7]]
```

## Key Takeaways
- Use four pointers to keep track of the current boundaries of the matrix.
- Fill the matrix in a spiral pattern by iterating over the elements in a clockwise direction.
- Continue until all elements are filled, adjusting the pointers as necessary to maintain the spiral pattern.