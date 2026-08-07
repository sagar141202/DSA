# Search a 2D Matrix

## Problem Statement
Given a 2D matrix of integers that is sorted in ascending order from left to right and top to bottom, write a function to search for a target integer in the matrix. The matrix can be empty, and the target integer may not exist in the matrix. The function should return true if the target integer exists in the matrix and false otherwise. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
and the target integer 5, the function should return true because 5 exists in the matrix.

## Approach
The approach is to treat the 2D matrix as a 1D array and perform a binary search. We can map the 2D coordinates to a 1D index using the formula `index = row * num_cols + col`. This allows us to search the matrix efficiently.

## Complexity
- Time: O(log(m*n))
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    if (matrix.empty() || matrix[0].empty()) return false;
    int rows = matrix.size();
    int cols = matrix[0].size();
    int left = 0;
    int right = rows * cols - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        int mid_val = matrix[mid / cols][mid % cols];
        if (mid_val == target) return true;
        else if (mid_val < target) left = mid + 1;
        else right = mid - 1;
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
- The key to this problem is to treat the 2D matrix as a 1D array and perform a binary search.
- The formula `index = row * num_cols + col` is used to map the 2D coordinates to a 1D index.
- The time complexity of this solution is O(log(m*n)), where m is the number of rows and n is the number of columns in the matrix.