# Search a 2D Matrix II

## Problem Statement
Write an efficient algorithm to search for a target value in a 2D matrix that is sorted in a specific way: each row is sorted in ascending order, and the last element of each row is less than or equal to the first element of the next row. The function should return true if the target is found, and false otherwise. The matrix can be empty, and the target value can be any integer. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
and the target value `5`, the function should return `true`.

## Approach
The algorithm starts from the top right corner of the matrix and compares the target value with the current element. If the target is less than the current element, it moves left; if the target is greater, it moves down. This approach takes advantage of the fact that the matrix is sorted in a specific way.

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
Input: 
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target: 5
Output: true

Input: 
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target: 20
Output: false
```

## Key Takeaways
- The algorithm takes advantage of the fact that the matrix is sorted in a specific way to achieve a time complexity of O(m + n).
- The space complexity is O(1) because only a constant amount of space is used.
- The algorithm starts from the top right corner of the matrix and moves either left or down based on the comparison with the target value.