# Search a 2D Matrix II

## Problem Statement
Write an efficient algorithm to search for a target value in a 2D matrix where each row is sorted in ascending order and each column is sorted in ascending order. The matrix does not necessarily have to be a square matrix. The algorithm should return true if the target is found, and false otherwise. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
and a target of 5, the algorithm should return true because 5 is present in the matrix.

## Approach
The algorithm will start from the top-right corner of the matrix and move either left or down based on the comparison of the current element with the target. This approach takes advantage of the fact that the rows and columns are sorted.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // Check if the matrix is empty
        if (matrix.empty() || matrix[0].empty()) {
            return false;
        }

        int row = 0;
        int col = matrix[0].size() - 1;

        // Continue the search until we are within the bounds of the matrix
        while (row < matrix.size() && col >= 0) {
            // If the current element is equal to the target, return true
            if (matrix[row][col] == target) {
                return true;
            }
            // If the current element is greater than the target, move left
            else if (matrix[row][col] > target) {
                col--;
            }
            // If the current element is less than the target, move down
            else {
                row++;
            }
        }

        // If we have searched the entire matrix and haven't found the target, return false
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
- The algorithm takes advantage of the fact that the rows and columns are sorted to reduce the search space.
- The time complexity is O(m + n) because in the worst case, we might have to traverse the entire matrix.
- The space complexity is O(1) because we only use a constant amount of space to store the current row and column indices.