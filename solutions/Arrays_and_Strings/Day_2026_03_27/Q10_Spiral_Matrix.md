# Spiral Matrix

## Problem Statement
Given a matrix of size m x n, write a function that traverses the matrix in a spiral order and returns the elements in the order they are visited. The matrix is filled with distinct integers. For example, given the following matrix:
```
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
```
The function should return `[1, 2, 3, 6, 9, 8, 7, 4, 5]`.

## Approach
The algorithm uses four pointers (top, bottom, left, right) to keep track of the current boundaries of the matrix. It iterates through the matrix in a spiral order by moving the pointers accordingly.

## Complexity
- Time: O(m * n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<int> spiralOrder(vector<vector<int>>& matrix) {
    vector<int> result;
    if (matrix.size() == 0) return result;

    int top = 0;
    int bottom = matrix.size() - 1;
    int left = 0;
    int right = matrix[0].size() - 1;

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
```

## Test Cases
```
Input: [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
```

## Key Takeaways
- Use four pointers to keep track of the current boundaries of the matrix.
- Traverse the matrix in a spiral order by moving the pointers accordingly.
- Handle edge cases where the matrix is empty or has only one row/column.