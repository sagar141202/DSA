# Spiral Matrix

## Problem Statement
Given a matrix of size m x n, write a function that traverses the matrix in a spiral order and returns the elements in a single array. The spiral order starts from the top left corner, goes to the right, then down, then left, and finally up, repeating this pattern until all elements are visited. The input matrix will contain integers and will not be empty. For example, given the following matrix:
```
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
```
The output should be: `[1, 2, 3, 6, 9, 8, 7, 4, 5]`.

## Approach
The algorithm uses four pointers to keep track of the current boundaries of the matrix. It starts by traversing from left to right, then down, then right to left, and finally up, updating the boundaries after each traversal. This process continues until all elements are visited.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <vector>

class Solution {
public:
    std::vector<int> spiralOrder(std::vector<std::vector<int>>& matrix) {
        std::vector<int> result;
        if (matrix.empty()) return result;

        int rowBegin = 0;
        int rowEnd = matrix.size() - 1;
        int colBegin = 0;
        int colEnd = matrix[0].size() - 1;

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
                rowEnd--;
            }

            // Traverse from bottom to top
            if (colBegin <= colEnd) {
                for (int i = rowEnd; i >= rowBegin; i--) {
                    result.push_back(matrix[i][colBegin]);
                }
                colBegin++;
            }
        }

        return result;
    }
};
```

## Test Cases
```
Input: [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
Input: [
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9,10,11,12]
]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
```

## Key Takeaways
- The spiral order traversal can be achieved by maintaining four pointers for the boundaries of the matrix.
- The algorithm iteratively updates these boundaries after each traversal.
- The time complexity is linear with respect to the total number of elements in the matrix.