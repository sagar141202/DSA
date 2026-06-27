# Search a 2D Matrix

## Problem Statement
Given a 2D matrix of integers and a target integer, write a function to search for the target in the matrix. The matrix is sorted in a way that all elements in each row are sorted in ascending order, and the first element of each row is greater than the last element of the previous row. The function should return true if the target is found in the matrix, and false otherwise. For example, given the matrix:
```
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
]
```
and the target `3`, the function should return `true`. If the target is `13`, the function should return `false`.

## Approach
We can treat the 2D matrix as a 1D sorted array and use binary search to find the target. The algorithm works by calculating the middle index of the array and comparing the middle element to the target.

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
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
], target = 3
Output: true

Input: matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
], target = 13
Output: false
```

## Key Takeaways
- The problem can be solved by treating the 2D matrix as a 1D sorted array.
- Binary search can be used to find the target in the array.
- The time complexity is O(log(m*n)) where m is the number of rows and n is the number of columns in the matrix.