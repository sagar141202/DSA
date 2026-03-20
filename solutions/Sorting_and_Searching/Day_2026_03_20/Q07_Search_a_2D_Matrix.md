# Search a 2D Matrix

## Problem Statement
Write a function to search for a target value in a 2D matrix, where each row is sorted in ascending order and each column is sorted in ascending order. The matrix does not contain duplicate values. The function should return `true` if the target is found and `false` otherwise. The matrix is represented as a vector of vectors, where each inner vector represents a row in the matrix. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
And the target value is `5`, the function should return `true`. If the target value is `20`, the function should return `false`.

## Approach
The algorithm starts from the top-right corner of the matrix and compares the target value with the current element. If the target is less than the current element, it moves left; otherwise, it moves down. This process continues until the target is found or the search space is exhausted.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    // Check if the matrix is empty
    if (matrix.empty() || matrix[0].empty()) {
        return false;
    }

    int rows = matrix.size();
    int cols = matrix[0].size();
    int row = 0;
    int col = cols - 1;

    // Start from the top-right corner and search for the target
    while (row < rows && col >= 0) {
        if (matrix[row][col] == target) {
            return true;
        } else if (matrix[row][col] > target) {
            // If the target is less than the current element, move left
            col--;
        } else {
            // If the target is greater than the current element, move down
            row++;
        }
    }

    // If the target is not found, return false
    return false;
}
```

## Test Cases
```
Input: matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], target = 5
Output: true

Input: matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], target = 20
Output: false
```

## Key Takeaways
- The algorithm takes advantage of the fact that the matrix is sorted in ascending order from left to right and top to bottom.
- By starting from the top-right corner, we can reduce the search space effectively.
- The time complexity is O(m + n), where m is the number of rows and n is the number of columns in the matrix.