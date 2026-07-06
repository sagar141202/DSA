# Search a 2D Matrix

## Problem Statement
Given a 2D matrix sorted in ascending order from left to right and top to bottom, write a function that searches for a target value in the matrix and returns its position if found, or -1 if not found. The matrix has 'm' rows and 'n' columns. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
and target value 5, the function should return [1,1] because the value 5 is at position (1,1) in the matrix (0-indexed).

## Approach
The algorithm treats the 2D matrix as a 1D sorted array and uses binary search to find the target value. It calculates the middle index of the virtual 1D array and compares the middle element with the target. If the target is found, its position is returned; otherwise, the search space is adjusted accordingly.

## Complexity
- Time: O(log(m*n))
- Space: O(1)

## C++ Solution
```cpp
#include <vector>

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
            int midVal = matrix[mid / n][mid % n];
            
            if (midVal == target) return true;
            else if (midVal < target) left = mid + 1;
            else right = mid - 1;
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
- The 2D matrix can be treated as a 1D sorted array to apply binary search.
- The mid index in the virtual 1D array is calculated using `mid / n` and `mid % n` to map it back to the 2D matrix coordinates.
- This approach reduces the time complexity to O(log(m*n)) compared to a linear search which would be O(m*n).