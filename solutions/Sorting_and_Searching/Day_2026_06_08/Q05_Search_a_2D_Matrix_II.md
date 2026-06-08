# Search a 2D Matrix II

## Problem Statement
Write a function to search for a target value in a 2D matrix where each row is sorted in ascending order, but the columns may not be sorted. The matrix can be empty, and the target value may not exist in the matrix. The function should return true if the target value exists in the matrix, and false otherwise. The input matrix is a vector of vectors, where each inner vector represents a row in the matrix. The target value is an integer. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
and the target value 5, the function should return true because 5 exists in the matrix.

## Approach
The algorithm starts from the top-right corner of the matrix and moves either down or left based on the comparison of the current element and the target value. This approach takes advantage of the fact that each row is sorted in ascending order.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    if (matrix.empty() || matrix[0].empty()) {
        return false;
    }
    int rows = matrix.size();
    int cols = matrix[0].size();
    int row = 0;
    int col = cols - 1;
    while (row < rows && col >= 0) {
        if (matrix[row][col] == target) {
            return true;
        } else if (matrix[row][col] < target) {
            row++;
        } else {
            col--;
        }
    }
    return false;
}
```

## Test Cases
```
Input: 
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Target: 5
Output: true

Input: 
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Target: 20
Output: false
```

## Key Takeaways
- Start from the top-right corner of the matrix to take advantage of the sorted rows.
- Move down if the current element is less than the target, and move left if the current element is greater than the target.
- Continue the search until the target is found or the search space is exhausted.