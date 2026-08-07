# Spiral Matrix

## Problem Statement
Given a matrix of size m x n, write a function that generates a spiral matrix, starting from the top-left corner and moving in a clockwise direction. The function should take two integers, m and n, as input and return a 2D vector representing the spiral matrix. For example, given m = 3 and n = 3, the function should return:
```
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
```
The constraints are 1 <= m <= 10 and 1 <= n <= 10.

## Approach
The algorithm uses four pointers to keep track of the current boundaries of the matrix. It iterates through the matrix in a spiral order, filling in the numbers from 1 to m*n. The pointers are updated after each iteration to move the boundaries inward.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<vector<int>> generateMatrix(int m, int n) {
    vector<vector<int>> matrix(m, vector<int>(n, 0));
    int top = 0, bottom = m - 1, left = 0, right = n - 1;
    int num = 1;
    
    while (top <= bottom && left <= right) {
        // Fill the top row from left to right
        for (int i = left; i <= right; i++) {
            matrix[top][i] = num++;
        }
        top++;
        
        // Fill the right column from top to bottom
        for (int i = top; i <= bottom; i++) {
            matrix[i][right] = num++;
        }
        right--;
        
        // Fill the bottom row from right to left
        if (top <= bottom) {
            for (int i = right; i >= left; i--) {
                matrix[bottom][i] = num++;
            }
            bottom--;
        }
        
        // Fill the left column from bottom to top
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
Input: m = 3, n = 3
Output: [
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

Input: m = 4, n = 4
Output: [
 [ 1, 2, 3, 4 ],
 [12, 13, 14, 5 ],
 [11, 16, 15, 6 ],
 [10, 9, 8, 7 ]
]
```

## Key Takeaways
- Use four pointers to keep track of the current boundaries of the matrix.
- Fill in the numbers in a spiral order by iterating through the matrix from top to bottom and left to right.
- Update the pointers after each iteration to move the boundaries inward.