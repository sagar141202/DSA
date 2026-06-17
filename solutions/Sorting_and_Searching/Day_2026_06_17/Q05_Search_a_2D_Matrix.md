# Search a 2D Matrix

## Problem Statement
Given a 2D matrix sorted in ascending order from left to right and top to bottom, write a function to search for a target value in the matrix. The matrix has 'n' rows and 'm' columns. The function should return true if the target is found, otherwise false. For example, given the matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
and the target value 5, the function should return true.

## Approach
The algorithm treats the 2D matrix as a 1D sorted array and uses binary search to find the target value. It calculates the middle index of the virtual 1D array and compares the middle element with the target. If the target is found, the function returns true; otherwise, it continues the search in the left or right half of the array.

## Complexity
- Time: O(log(n*m))
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    if (matrix.empty() || matrix[0].empty()) {
        return false;
    }
    
    int n = matrix.size();
    int m = matrix[0].size();
    int left = 0;
    int right = n * m - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        int mid_val = matrix[mid / m][mid % m];
        
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
- The problem can be solved by treating the 2D matrix as a 1D sorted array.
- Binary search is an efficient algorithm for finding an element in a sorted array.
- The time complexity of the solution is O(log(n*m)), where 'n' is the number of rows and 'm' is the number of columns in the matrix.