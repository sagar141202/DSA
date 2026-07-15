# Search a 2D Matrix II

## Problem Statement
Write a function that searches for a target value in a 2D matrix where each row is sorted in ascending order and each column is sorted in ascending order. The function should return true if the target is found and false otherwise. The matrix is not necessarily a square matrix. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
and the target `5`, the function should return `true`. If the target is `20`, the function should return `false`. The matrix can contain duplicate values.

## Approach
The algorithm starts from the top-right corner of the matrix and compares the target value with the current element. If the target is less than the current element, it moves left; otherwise, it moves down. This process continues until the target is found or the matrix boundaries are exceeded.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    if (matrix.empty() || matrix[0].empty()) return false;
    
    int row = 0, col = matrix[0].size() - 1;
    while (row < matrix.size() && col >= 0) {
        if (matrix[row][col] == target) return true;
        else if (matrix[row][col] < target) row++;
        else col--;
    }
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
- Start from the top-right corner of the matrix to take advantage of the sorted rows and columns.
- Compare the target value with the current element and move accordingly to reduce the search space.
- Use a while loop to continue the search until the target is found or the matrix boundaries are exceeded.