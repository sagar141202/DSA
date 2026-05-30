# Search a 2D Matrix

## Problem Statement
Given a 2D matrix sorted in ascending order from left to right and top to bottom, write a function that searches for a target value in the matrix. The matrix has the following properties: 
- Each row is sorted in ascending order from left to right.
- Each column is sorted in ascending order from top to bottom.
For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
And a target value of `5`, the function should return `true` because `5` is present in the matrix. If the target value is `20`, the function should return `false` because `20` is not present in the matrix.

## Approach
We will treat the 2D matrix as a 1D sorted array and use a binary search algorithm to find the target value. We will calculate the middle index of the array and compare the middle element with the target value.

## Complexity
- Time: O(log(m*n))
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
        int left = 0;
        int right = rows * cols - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int midVal = matrix[mid / cols][mid % cols];
            
            if (midVal == target) {
                return true;
            } else if (midVal < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
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
- The 2D matrix can be treated as a 1D sorted array.
- Binary search can be used to find the target value in the matrix.
- The time complexity of the solution is O(log(m*n)), where m is the number of rows and n is the number of columns in the matrix.