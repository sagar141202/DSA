# Search a 2D Matrix

## Problem Statement
Given a 2D matrix of integers that is sorted in ascending order from left to right and top to bottom, write a function to search for a target number in the matrix. The matrix can be empty, and the target number may not exist in the matrix. The function should return true if the target number exists in the matrix and false otherwise. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
and target number 5, the function should return true because 5 exists in the matrix.

## Approach
We can treat the 2D matrix as a 1D sorted array and use binary search to find the target number. The key is to map the 1D index to the 2D coordinates. We start by calculating the middle index of the 1D array and then map it to the 2D coordinates. If the middle element is equal to the target, we return true. If the middle element is less than the target, we search in the right half of the 1D array. If the middle element is greater than the target, we search in the left half of the 1D array.

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
        int m = matrix.size();
        int n = matrix[0].size();
        int left = 0;
        int right = m * n - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int midVal = matrix[mid / n][mid % n];
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
```

## Key Takeaways
- Treat the 2D matrix as a 1D sorted array to simplify the problem.
- Use binary search to find the target number in the 1D array.
- Map the 1D index to the 2D coordinates using integer division and modulo operations.