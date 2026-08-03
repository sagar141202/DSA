# Search a 2D Matrix

## Problem Statement
Write a function that searches for a target value in a 2D matrix, where each row is sorted in ascending order and each column is sorted in ascending order. The function should return true if the target value is found, and false otherwise. The input matrix will have at least one row and one column, and all elements will be integers. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
and a target value of 5, the function should return true.

## Approach
We can solve this problem by starting from the top-right corner of the matrix and moving either left or down depending on whether the target value is less than or greater than the current element. This approach takes advantage of the fact that the rows and columns are sorted.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // Start from the top-right corner of the matrix
        int row = 0;
        int col = matrix[0].size() - 1;
        
        // Continue searching while we are within the bounds of the matrix
        while (row < matrix.size() && col >= 0) {
            // If the target value is found, return true
            if (matrix[row][col] == target) {
                return true;
            }
            // If the target value is less than the current element, move left
            else if (matrix[row][col] > target) {
                col--;
            }
            // If the target value is greater than the current element, move down
            else {
                row++;
            }
        }
        
        // If the target value is not found, return false
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
- The problem can be solved by taking advantage of the fact that the rows and columns are sorted.
- We can start from the top-right corner of the matrix and move either left or down depending on whether the target value is less than or greater than the current element.
- The time complexity of the solution is O(m + n), where m is the number of rows and n is the number of columns.