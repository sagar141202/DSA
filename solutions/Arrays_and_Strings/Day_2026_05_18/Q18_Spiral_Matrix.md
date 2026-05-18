# Spiral Matrix

## Problem Statement
Given a matrix of size m x n, write a function that fills the matrix with numbers from 1 to m*n in a spiral order, starting from the top left corner and moving clockwise. The function should take two integers m and n as input and return the filled matrix. For example, if m = 3 and n = 3, the output should be:
```
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
```
The constraints are 1 <= m <= 10^3 and 1 <= n <= 10^3.

## Approach
The algorithm uses four pointers (top, bottom, left, right) to represent the current boundaries of the matrix. It fills the matrix in a spiral order by iterating through the elements in a clockwise direction. The algorithm continues until all elements are filled.

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
Output: 
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
Input: m = 4, n = 5
Output: 
[
 [ 1, 2, 3, 4, 5 ],
 [ 14, 15, 16, 17, 6 ],
 [ 13, 20, 19, 18, 7 ],
 [ 12, 11, 10, 9, 8 ]
]
```

## Key Takeaways
- The algorithm uses four pointers to represent the current boundaries of the matrix.
- The algorithm fills the matrix in a spiral order by iterating through the elements in a clockwise direction.
- The time complexity is O(m*n) and the space complexity is O(m*n), where m and n are the dimensions of the matrix.