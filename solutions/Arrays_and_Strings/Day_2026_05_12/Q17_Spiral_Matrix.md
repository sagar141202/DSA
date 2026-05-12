# Spiral Matrix

## Problem Statement
Given a matrix of size m x n, write a function that traverses the matrix in a spiral order and returns the elements in the order they are visited. The spiral order starts from the top left, goes right, then down, then left, and then up, repeating the process until all elements are visited. The input matrix is a 2D vector of integers, where 1 <= m, n <= 10. For example, given the following matrix:
```
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
```
The output should be: [1, 2, 3, 6, 9, 8, 7, 4, 5].

## Approach
The algorithm uses four pointers to keep track of the current boundaries of the matrix. It starts by iterating from left to right, then from top to bottom, then from right to left, and finally from bottom to top, updating the boundaries after each iteration.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<int> spiralOrder(vector<vector<int>>& matrix) {
    vector<int> result;
    if (matrix.empty()) return result;
    int rowBegin = 0, rowEnd = matrix.size() - 1;
    int colBegin = 0, colEnd = matrix[0].size() - 1;
    while (rowBegin <= rowEnd && colBegin <= colEnd) {
        // Traverse from left to right
        for (int i = colBegin; i <= colEnd; i++) {
            result.push_back(matrix[rowBegin][i]);
        }
        rowBegin++;
        
        // Traverse from top to bottom
        for (int i = rowBegin; i <= rowEnd; i++) {
            result.push_back(matrix[i][colEnd]);
        }
        colEnd--;
        
        // Traverse from right to left
        if (rowBegin <= rowEnd) {
            for (int i = colEnd; i >= colBegin; i--) {
                result.push_back(matrix[rowEnd][i]);
            }
        }
        rowEnd--;
        
        // Traverse from bottom to top
        if (colBegin <= colEnd) {
            for (int i = rowEnd; i >= rowBegin; i--) {
                result.push_back(matrix[i][colBegin]);
            }
        }
        colBegin++;
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
- Use four pointers to track the current boundaries of the matrix.
- Update the boundaries after each iteration to ensure all elements are visited.
- Handle edge cases where the matrix is empty or has only one row or column.