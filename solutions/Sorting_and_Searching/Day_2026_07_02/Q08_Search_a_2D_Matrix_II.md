# Search a 2D Matrix II

## Problem Statement
Write a function that searches for a target value in a 2D matrix, where each row is sorted in ascending order and each column is sorted in ascending order. The function should return true if the target is found, and false otherwise. The input matrix will have at least one row and one column. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
and target `5`, the function should return `true`. If the target is `20`, the function should return `false`.

## Approach
We can solve this problem by starting from the top right corner of the matrix and moving either left or down based on the comparison of the current element with the target. This approach ensures that we are always moving towards the target.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    // start from the top right corner
    int row = 0;
    int col = matrix[0].size() - 1;
    
    // continue the search until we are within the matrix bounds
    while (row < matrix.size() && col >= 0) {
        // if the current element is equal to the target, return true
        if (matrix[row][col] == target) {
            return true;
        }
        // if the current element is greater than the target, move left
        else if (matrix[row][col] > target) {
            col--;
        }
        // if the current element is less than the target, move down
        else {
            row++;
        }
    }
    
    // if we have searched the entire matrix and haven't found the target, return false
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
- Start from the top right corner of the matrix to take advantage of the sorted rows and columns.
- Move either left or down based on the comparison of the current element with the target.
- Continue the search until we are within the matrix bounds or we find the target.