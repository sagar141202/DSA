# Spiral Matrix

## Problem Statement
Given a matrix of size `m x n`, generate a spiral matrix where elements are filled in a spiral order, starting from the top left and moving clockwise. The matrix should be filled with numbers from 1 to `m * n`. For example, given `m = 3` and `n = 4`, the output should be:
```
[
 [ 1, 2, 3, 4 ],
 [ 5, 6, 7, 8 ],
 [ 9,10,11,12 ]
]
```
The constraints are `1 <= m <= 10^3` and `1 <= n <= 10^3`.

## Approach
The algorithm uses four pointers to track the current boundaries of the matrix. It fills the matrix in a spiral order by iterating over the elements in a clockwise direction. The pointers are updated after each iteration to move towards the center of the matrix.

## Complexity
- Time: O(m * n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>

vector<vector<int>> generateMatrix(int m, int n) {
    vector<vector<int>> matrix(m, vector<int>(n, 0));
    int top = 0, bottom = m - 1, left = 0, right = n - 1;
    int num = 1;
    while (top <= bottom && left <= right) {
        // Fill the top row
        for (int i = left; i <= right; i++) {
            matrix[top][i] = num++;
        }
        top++;
        
        // Fill the right column
        for (int i = top; i <= bottom; i++) {
            matrix[i][right] = num++;
        }
        right--;
        
        // Fill the bottom row
        if (top <= bottom) {
            for (int i = right; i >= left; i--) {
                matrix[bottom][i] = num++;
            }
            bottom--;
        }
        
        // Fill the left column
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
Input: m = 3, n = 4
Output: [
 [ 1, 2, 3, 4 ],
 [ 5, 6, 7, 8 ],
 [ 9,10,11,12 ]
]
```

## Key Takeaways
- Use four pointers to track the current boundaries of the matrix.
- Fill the matrix in a spiral order by iterating over the elements in a clockwise direction.
- Update the pointers after each iteration to move towards the center of the matrix.