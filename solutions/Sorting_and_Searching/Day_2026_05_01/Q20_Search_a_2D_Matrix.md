# Search a 2D Matrix

## Problem Statement
Given a 2D matrix of integers and a target value, write a function that searches for the target in the matrix. The matrix has the following properties: each row is sorted in ascending order, and each column is sorted in ascending order. If the target is found, return true; otherwise, return false. The matrix can be empty, and the target can be any integer. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
and the target `5`, the function should return `true`.

## Approach
We can solve this problem by starting from the top-right corner of the matrix and moving either left or down based on the comparison between the current element and the target. This approach takes advantage of the fact that each row and column is sorted.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) {
            return false;
        }
        
        int rows = matrix.size();
        int cols = matrix[0].size();
        int row = 0;
        int col = cols - 1;
        
        while (row < rows && col >= 0) {
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
- The problem can be solved by taking advantage of the fact that each row and column is sorted.
- The time complexity is O(m + n), where m is the number of rows and n is the number of columns.
- The space complexity is O(1), as we only use a constant amount of space to store the row and column indices.