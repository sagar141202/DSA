# Search a 2D Matrix

## Problem Statement
Write an efficient algorithm to search for a target element in a 2D matrix that is sorted in a specific way: each row is sorted in ascending order, and the last element of each row is less than or equal to the first element of the next row. The matrix can be very large, so an efficient solution is required. For example, given the following matrix:
```
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
```
and a target element `3`, the algorithm should return `true` if the target element is present in the matrix, and `false` otherwise.

## Approach
The algorithm will treat the 2D matrix as a 1D sorted array and use a modified binary search algorithm to find the target element. The idea is to map the 2D coordinates to a 1D index and then perform a binary search. This approach takes advantage of the fact that the matrix is sorted in a specific way.

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
        if (matrix.empty() || matrix[0].empty()) return false;
        
        int m = matrix.size();
        int n = matrix[0].size();
        
        int left = 0;
        int right = m * n - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int mid_val = matrix[mid / n][mid % n];
            
            if (mid_val == target) return true;
            else if (mid_val < target) left = mid + 1;
            else right = mid - 1;
        }
        
        return false;
    }
};
```

## Test Cases
```
Input: matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], target = 3
Output: true

Input: matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], target = 13
Output: false
```

## Key Takeaways
- The 2D matrix can be treated as a 1D sorted array by mapping the 2D coordinates to a 1D index.
- A modified binary search algorithm can be used to find the target element in the matrix.
- The time complexity of the algorithm is O(log(m*n)), making it efficient for large matrices.