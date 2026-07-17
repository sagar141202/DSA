# Search a 2D Matrix II

## Problem Statement
Write an efficient algorithm to search for a target value in a 2D matrix, where each row is sorted in ascending order, but the columns may not be sorted. The matrix can contain duplicate values, and the target value can appear multiple times. The algorithm should return true if the target value is found, and false otherwise. The input matrix will have dimensions m x n, where m and n are positive integers. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
And the target value is 5, the algorithm should return true, because 5 is present in the matrix.

## Approach
The algorithm will use a modified binary search approach, starting from the top-right corner of the matrix. It will compare the target value with the current element and move either left or down based on the comparison. This approach takes advantage of the fact that each row is sorted in ascending order.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
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
            } else if (matrix[row][col] > target) {
                col--;
            } else {
                row++;
            }
        }

        return false;
    }
};
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
- The algorithm starts from the top-right corner of the matrix and moves either left or down based on the comparison with the target value.
- The time complexity is O(m + n), where m and n are the dimensions of the matrix, because in the worst case, the algorithm needs to traverse the entire matrix.
- The space complexity is O(1), because the algorithm only uses a constant amount of space to store the row and column indices.