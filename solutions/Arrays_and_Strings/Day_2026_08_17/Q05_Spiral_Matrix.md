# Spiral Matrix

## Problem Statement
Given a matrix of size m x n, write a function that traverses the matrix in a spiral order and returns the elements in the order they were visited. The spiral order starts from the top-left corner and moves clockwise. The function should take as input a 2D vector of integers representing the matrix and return a vector of integers representing the spiral order. For example, given the following matrix:
```
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
```
The function should return the vector `[1, 2, 3, 6, 9, 8, 7, 4, 5]`. The matrix can be of any size and can contain any integers.

## Approach
The algorithm uses four pointers to keep track of the current boundaries of the matrix. It iterates over the elements in a spiral order by moving the pointers in a clockwise direction. The pointers are updated after each iteration to ensure that the algorithm stays within the boundaries of the matrix.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<int> spiralOrder(vector<vector<int>>& matrix) {
    vector<int> result;
    if (matrix.empty()) return result;
    
    int rowStart = 0, rowEnd = matrix.size();
    int colStart = 0, colEnd = matrix[0].size();
    
    while (rowStart < rowEnd && colStart < colEnd) {
        // Traverse from left to right
        for (int i = colStart; i < colEnd; i++) {
            result.push_back(matrix[rowStart][i]);
        }
        rowStart++;
        
        // Traverse from top to bottom
        for (int i = rowStart; i < rowEnd; i++) {
            result.push_back(matrix[i][colEnd - 1]);
        }
        colEnd--;
        
        // Traverse from right to left
        if (rowStart < rowEnd) {
            for (int i = colEnd - 1; i >= colStart; i--) {
                result.push_back(matrix[rowEnd - 1][i]);
            }
            rowEnd--;
        }
        
        // Traverse from bottom to top
        if (colStart < colEnd) {
            for (int i = rowEnd - 1; i >= rowStart; i--) {
                result.push_back(matrix[i][colStart]);
            }
            colStart++;
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
- The spiral order traversal can be achieved by maintaining four pointers to track the current boundaries of the matrix.
- The algorithm iterates over the elements in a spiral order by moving the pointers in a clockwise direction.
- The time complexity of the algorithm is O(m * n), where m is the number of rows and n is the number of columns in the matrix.