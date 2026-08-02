# Search a 2D Matrix II

## Problem Statement
Write an efficient algorithm to search for a target value in a 2D matrix where each row is sorted in ascending order and each column is also sorted in ascending order. The matrix does not necessarily have to be a square matrix. The algorithm should return true if the target is found, and false otherwise. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
and a target value of 5, the algorithm should return true. If the target value is 20, the algorithm should return false.

## Approach
The algorithm will start from the top-right corner of the matrix and compare the target value with the current element. If the target is less than the current element, it will move left, otherwise, it will move down. This approach takes advantage of the fact that the rows and columns are sorted.

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
        if (matrix.empty() || matrix[0].empty()) return false;
        
        int row = 0, col = matrix[0].size() - 1;
        while (row < matrix.size() && col >= 0) {
            if (matrix[row][col] == target) return true;
            else if (matrix[row][col] < target) row++;
            else col--;
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
- The algorithm takes advantage of the fact that the rows and columns are sorted.
- The time complexity is O(m + n) where m is the number of rows and n is the number of columns.
- The space complexity is O(1) as no extra space is used.