# Spiral Matrix

## Problem Statement
Given a matrix of size m x n, write a function that traverses the matrix in a spiral order and returns the elements in the order they are visited. The spiral order starts from the top left, goes to the right, then down, then left, and finally up. The function should take as input the number of rows (m) and columns (n) in the matrix, and return a vector of integers representing the spiral order of the matrix elements. For example, given a 3x3 matrix:
```
1 2 3
4 5 6
7 8 9
```
The spiral order is: `[1, 2, 3, 6, 9, 8, 7, 4, 5]`.

## Approach
The algorithm uses four pointers (top, bottom, left, right) to track the current boundaries of the matrix. It iteratively visits the elements in the spiral order by moving the pointers and adding the elements to the result vector.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<int> spiralOrder(vector<vector<int>>& matrix) {
    if (matrix.empty()) return {};
    int rows = matrix.size(), cols = matrix[0].size();
    int top = 0, bottom = rows - 1, left = 0, right = cols - 1;
    vector<int> result;
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
Input: 
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
```

## Key Takeaways
- Initialize four pointers (top, bottom, left, right) to track the current boundaries of the matrix.
- Iterate through the matrix in a spiral order by moving the pointers and adding the elements to the result vector.
- Use conditional statements to handle edge cases where the matrix has an odd number of rows or columns.