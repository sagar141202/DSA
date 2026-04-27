# Search a 2D Matrix

## Problem Statement
Write a function to search for a target value in a 2D matrix sorted in ascending order from left to right and top to bottom. The matrix has 'm' rows and 'n' columns. The function should return true if the target is found, and false otherwise. The matrix is sorted such that for any given row, all elements to its left are smaller, and for any given column, all elements above it are smaller. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
And the target is 5, the function should return true because 5 is present in the matrix.

## Approach
The algorithm treats the 2D matrix as a 1D sorted array and uses binary search to find the target. It maps the 1D index to the corresponding 2D coordinates using the formula `index = row * n + col`, where 'n' is the number of columns.

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
        int m = matrix.size();
        int n = matrix[0].size();
        
        int left = 0;
        int right = m * n - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int mid_val = matrix[mid / n][mid % n];
            
            if (mid_val == target) {
                return true;
            } else if (mid_val < target) {
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
- Treat the 2D matrix as a 1D sorted array to simplify the problem.
- Use binary search to find the target in the sorted array.
- Map the 1D index to the corresponding 2D coordinates using the formula `index = row * n + col`.