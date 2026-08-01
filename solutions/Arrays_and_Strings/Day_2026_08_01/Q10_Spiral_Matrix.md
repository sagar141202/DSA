# Spiral Matrix

## Problem Statement
Given a matrix of size m x n, write a function that traverses the matrix in a spiral order and returns the elements in the order they are visited. The spiral order starts from the top left corner, goes right, then down, then left, and then up, repeating the process until all elements are visited. The input matrix is a 2D vector of integers, and the output is a 1D vector of integers. For example, given the input matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]], the output should be [1, 2, 3, 6, 9, 8, 7, 4, 5].

## Approach
The algorithm uses four pointers to keep track of the current boundaries of the matrix. It iterates through the elements in a spiral order by moving the pointers inward after each iteration. The spiral order is achieved by first moving right, then down, then left, and finally up.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
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
};
```

## Test Cases
```
Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
Input: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
```

## Key Takeaways
- Use four pointers to keep track of the current boundaries of the matrix.
- Move the pointers inward after each iteration to achieve the spiral order.
- Handle edge cases where the matrix is empty or has only one row or column.