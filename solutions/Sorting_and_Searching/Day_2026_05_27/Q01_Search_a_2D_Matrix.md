# Search a 2D Matrix

## Problem Statement
Write a function that searches for a target value in a 2D matrix, where each row is sorted in ascending order and each column is sorted in ascending order. The function should return `true` if the target is found and `false` otherwise. The input matrix is a 2D vector of integers, and the target is an integer. The matrix can be empty, and the function should handle this case correctly. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
and a target of `5`, the function should return `true` because `5` is in the matrix.

## Approach
We can start from the top right corner of the matrix and move left if the target is smaller than the current element, or move down if the target is larger. This approach takes advantage of the fact that each row and column is sorted.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) {
            return false;
        }
        
        int row = 0;
        int col = matrix[0].size() - 1;
        
        while (row < matrix.size() && col >= 0) {
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
- Start from the top right corner of the matrix to take advantage of the sorted rows and columns.
- Move left if the target is smaller than the current element, or move down if the target is larger.
- Handle the case where the matrix is empty.