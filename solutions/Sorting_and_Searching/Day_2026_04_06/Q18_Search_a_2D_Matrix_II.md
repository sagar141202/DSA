# Search a 2D Matrix II

## Problem Statement
Write a function that searches for a target value in a 2D matrix. The matrix is sorted in ascending order from left to right and from top to bottom. The function should return true if the target is found, and false otherwise. The matrix is not necessarily a square matrix, and the number of rows and columns can vary. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
and a target of 5, the function should return true. If the target is 20, the function should return false.

## Approach
The algorithm starts from the top right corner of the matrix and compares the target with the current element. If the target is less than the current element, it moves left; otherwise, it moves down. This process continues until the target is found or the search space is exhausted.

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
        // start from the top right corner
        int row = 0;
        int col = matrix[0].size() - 1;
        
        while (row < matrix.size() && col >= 0) {
            // if the target is found, return true
            if (matrix[row][col] == target) {
                return true;
            }
            // if the target is less than the current element, move left
            else if (matrix[row][col] > target) {
                col--;
            }
            // if the target is greater than the current element, move down
            else {
                row++;
            }
        }
        // if the target is not found, return false
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
- The algorithm takes advantage of the sorted property of the matrix to reduce the search space.
- The time complexity is O(m + n), where m is the number of rows and n is the number of columns.
- The space complexity is O(1), as only a constant amount of space is used.