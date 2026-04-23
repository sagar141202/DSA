# Search a 2D Matrix II

## Problem Statement
Write an efficient algorithm to search for a target value in a 2D matrix. The matrix has the following properties: 
- The matrix is sorted in ascending order from left to right and from top to bottom.
- The matrix does not contain duplicate values.
- The matrix has 'n' rows and 'm' columns.
- The target value can be any integer.
- The function should return true if the target is found in the matrix, otherwise return false.
- Example:
  - Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
  - Output: true
  - Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
  - Output: false

## Approach
We can use a modified binary search algorithm to search for the target in the 2D matrix. Starting from the top-right corner of the matrix, we compare the target with the current element and move either left or down based on whether the target is smaller or larger.

## Complexity
- Time: O(n + m)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // Check if the matrix is empty
        if (matrix.empty() || matrix[0].empty()) {
            return false;
        }

        int rows = matrix.size();
        int cols = matrix[0].size();
        int row = 0;
        int col = cols - 1;

        // Start searching from the top-right corner
        while (row < rows && col >= 0) {
            if (matrix[row][col] == target) {
                return true;
            } else if (matrix[row][col] > target) {
                // Move left
                col--;
            } else {
                // Move down
                row++;
            }
        }

        return false;
    }
};
```

## Test Cases
```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
```

## Key Takeaways
- The algorithm starts from the top-right corner of the matrix and moves either left or down based on the comparison with the target.
- The time complexity is O(n + m) where 'n' is the number of rows and 'm' is the number of columns in the matrix.
- The space complexity is O(1) as we only use a constant amount of space to store the row and column indices.