# Search a 2D Matrix

## Problem Statement
Write a function that searches for a target value in a 2D matrix where each row is sorted in ascending order and each column is also sorted in ascending order. The function should return true if the target value exists in the matrix, and false otherwise. The input matrix is a 2D vector of integers, and the target value is an integer. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
And the target value is 5, the function should return true because 5 exists in the matrix.

## Approach
The algorithm starts from the top-right corner of the matrix and moves either left or down based on the comparison between the current element and the target value. This approach takes advantage of the fact that the rows and columns are sorted. By moving left if the current element is greater than the target, and moving down if it's less than the target, we can effectively search for the target in the matrix.

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
- The search starts from the top-right corner of the matrix to take advantage of the sorted rows and columns.
- The algorithm moves left if the current element is greater than the target, and moves down if it's less than the target.
- The time complexity is O(m + n) because in the worst case, we might need to traverse all rows and columns.