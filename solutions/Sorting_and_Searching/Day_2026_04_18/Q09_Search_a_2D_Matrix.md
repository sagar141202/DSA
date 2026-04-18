# Search a 2D Matrix

## Problem Statement
Given a 2D matrix of integers and a target integer, write a function that searches for the target in the matrix. The matrix has the following properties: 
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.
Example:
```
Input: matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], target = 3
Output: true
```
Constraints: 
- 1 <= matrix.length <= 100
- 1 <= matrix[i].length <= 100
- -10^4 <= matrix[i][j], target <= 10^4

## Approach
The approach is to treat the 2D matrix as a 1D sorted array and use binary search to find the target. 
This is possible due to the properties of the matrix where each row is sorted and the first element of each row is greater than the last element of the previous row.
We can calculate the middle index of the virtual 1D array and then map it to the corresponding row and column in the 2D matrix.

## Complexity
- Time: O(log(m*n))
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

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
- The 2D matrix can be treated as a 1D sorted array due to its properties.
- Binary search can be used to find the target in the matrix efficiently.
- The time complexity of the solution is O(log(m*n)), where m is the number of rows and n is the number of columns in the matrix.