# Spiral Matrix

## Problem Statement
Given an m x n matrix, return all elements of the matrix in spiral order. The matrix is filled with distinct positive integers. The spiral order starts from the top left and goes clockwise. For example, given the following matrix:
```
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
```
The output should be: `[1, 2, 3, 6, 9, 8, 7, 4, 5]`. The constraints are: `m == matrix.length`, `n == matrix[i].length`, `1 <= m, n <= 20`, and `1 <= matrix[i][j] <= 10^4`.

## Approach
The algorithm uses four pointers (top, bottom, left, right) to track the current boundaries of the matrix. It iterates through the matrix in a spiral order by moving the pointers accordingly. The spiral order is achieved by first traversing from left to right, then from top to bottom, then from right to left, and finally from bottom to top.

## Complexity
- Time: O(m * n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<int> spiralOrder(vector<vector<int>>& matrix) {
    vector<int> result;
    if (matrix.empty()) return result;
    
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
- Initialize four pointers to track the current boundaries of the matrix.
- Traverse the matrix in a spiral order by moving the pointers accordingly.
- Use conditional statements to handle edge cases where the matrix has an odd number of rows or columns.