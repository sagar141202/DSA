# Spiral Matrix

## Problem Statement
Given an m x n matrix, return all elements of the matrix in spiral order. The matrix is filled with distinct positive integers. The constraints are 1 <= m <= 10^3, 1 <= n <= 10^3, and 1 <= m * n <= 10^6. For example, given the input `matrix = [[1,2,3],[4,5,6],[7,8,9]]`, the output should be `[1,2,3,6,9,8,7,4,5]`.

## Approach
The algorithm uses four pointers (top, bottom, left, right) to traverse the matrix in a spiral order. It starts from the outermost layer and moves inwards. The pointers are updated after each traversal to ensure the spiral order is maintained.

## Complexity
- Time: O(m * n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>

vector<int> spiralOrder(std::vector<std::vector<int>>& matrix) {
    if (matrix.empty()) return {};
    
    int top = 0, bottom = matrix.size() - 1;
    int left = 0, right = matrix[0].size() - 1;
    std::vector<int> result;
    result.reserve(matrix.size() * matrix[0].size());
    
    while (top <= bottom && left <= right) {
        // Traverse from left to right
        for (int i = left; i <= right; ++i) {
            result.push_back(matrix[top][i]);
        }
        top++;
        
        // Traverse from top to bottom
        for (int i = top; i <= bottom; ++i) {
            result.push_back(matrix[i][right]);
        }
        right--;
        
        // Traverse from right to left
        if (top <= bottom) {
            for (int i = right; i >= left; --i) {
                result.push_back(matrix[bottom][i]);
            }
            bottom--;
        }
        
        // Traverse from bottom to top
        if (left <= right) {
            for (int i = bottom; i >= top; --i) {
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
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Input: [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## Key Takeaways
- The spiral order traversal can be achieved by maintaining four pointers (top, bottom, left, right) and updating them after each traversal.
- The time complexity is O(m * n) because we visit each element in the matrix once.
- The space complexity is O(1) if we do not consider the space required for the output, otherwise it is O(m * n) for storing the result.