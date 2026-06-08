# Search a 2D Matrix

## Problem Statement
Given a 2D matrix of integers sorted in ascending order from left to right and top to bottom, write a function to search for a target value in the matrix. The matrix has 'n' rows and 'm' columns. The function should return true if the target value is found, and false otherwise. For example, given the matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
and the target value 5, the function should return true because 5 is present in the matrix.

## Approach
The approach is to treat the 2D matrix as a 1D sorted array and use binary search to find the target value. This is possible because the matrix is sorted from left to right and top to bottom. We can calculate the middle index of the 1D array and then convert it to the corresponding row and column indices in the 2D matrix.

## Complexity
- Time: O(log(n*m))
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // Check if the matrix is empty
        if (matrix.empty() || matrix[0].empty()) {
            return false;
        }
        
        // Get the number of rows and columns
        int n = matrix.size();
        int m = matrix[0].size();
        
        // Define the binary search range
        int left = 0;
        int right = n * m - 1;
        
        // Perform binary search
        while (left <= right) {
            // Calculate the middle index
            int mid = left + (right - left) / 2;
            
            // Convert the middle index to row and column indices
            int midValue = matrix[mid / m][mid % m];
            
            // Check if the middle value is equal to the target
            if (midValue == target) {
                return true;
            }
            // If the middle value is less than the target, move to the right half
            else if (midValue < target) {
                left = mid + 1;
            }
            // If the middle value is greater than the target, move to the left half
            else {
                right = mid - 1;
            }
        }
        
        // If the target is not found, return false
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
- The 2D matrix can be treated as a 1D sorted array by using the row and column indices to calculate the corresponding index in the 1D array.
- Binary search can be used to find the target value in the 1D array, which corresponds to the 2D matrix.
- The time complexity of the solution is O(log(n*m)), where 'n' is the number of rows and 'm' is the number of columns in the matrix.