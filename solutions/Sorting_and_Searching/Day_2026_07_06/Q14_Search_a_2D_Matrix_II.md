# Search a 2D Matrix II

## Problem Statement
Write a function that searches for a target value in a 2D matrix where each row is sorted in ascending order and each column is sorted in ascending order. The function should return true if the target is found, and false otherwise. The matrix is not necessarily square and can have different numbers of rows and columns. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
And a target of 5, the function should return true because 5 is in the matrix. If the target is 20, the function should return false.

## Approach
The algorithm starts from the top right corner of the matrix and moves either left or down depending on whether the current value is greater than or less than the target. This approach takes advantage of the fact that the rows and columns are sorted.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;
        
        int row = 0, col = matrix[0].size() - 1;
        while (row < matrix.size() && col >= 0) {
            if (matrix[row][col] == target) return true;
            if (matrix[row][col] < target) row++;
            else col--;
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
- The key to solving this problem efficiently is to take advantage of the fact that both rows and columns are sorted.
- Starting from the top right corner allows us to make a decision based on the comparison with the target, effectively reducing the search space.
- This solution has a linear time complexity with respect to the sum of the number of rows and columns, making it efficient for large matrices.