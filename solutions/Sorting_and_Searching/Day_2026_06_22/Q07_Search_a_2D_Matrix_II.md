# Search a 2D Matrix II

## Problem Statement
Write an efficient algorithm to search for a target value in a 2D matrix where each row is sorted in ascending order and each column is sorted in ascending order. The matrix does not necessarily have the same number of rows and columns. The algorithm should return true if the target is found, and false otherwise. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
And target = 5, the algorithm should return true because 5 is in the matrix.

## Approach
The algorithm will start from the top right corner of the matrix and move left if the target is smaller than the current value, or move down if the target is larger. This approach takes advantage of the fact that the rows and columns are sorted. The algorithm will continue until it finds the target or reaches a point where it cannot move further.

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
            else if (matrix[row][col] > target) col--;
            else row++;
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
- The time complexity is O(m + n) because in the worst case, the algorithm will move through all rows and columns.
- The space complexity is O(1) because the algorithm only uses a constant amount of space to store the current position and the target value.