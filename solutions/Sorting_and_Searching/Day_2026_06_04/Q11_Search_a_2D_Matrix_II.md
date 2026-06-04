# Search a 2D Matrix II

## Problem Statement
Write a function that searches for a target value in a 2D matrix where each row is sorted in ascending order and each column is also sorted in ascending order. The matrix does not necessarily have to be a square matrix. The function should return true if the target is found, and false otherwise. The input matrix will have at least one row and one column. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
And the target is 5, the function should return true because 5 is in the matrix. If the target is 20, the function should return false because 20 is not in the matrix.

## Approach
We start from the top right corner of the matrix and move either left or down depending on whether the target is less than or greater than the current element. This approach works because the matrix is sorted in ascending order both row-wise and column-wise.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int m = matrix.size();
    int n = matrix[0].size();
    int row = 0;
    int col = n - 1;
    
    while (row < m && col >= 0) {
        if (matrix[row][col] == target) {
            return true;
        } else if (matrix[row][col] > target) {
            col--;
        } else {
            row++;
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
- The time complexity is O(m + n) where m is the number of rows and n is the number of columns in the matrix.
- The space complexity is O(1) as we are not using any extra space.
- The approach works by starting from the top right corner of the matrix and moving either left or down depending on whether the target is less than or greater than the current element.