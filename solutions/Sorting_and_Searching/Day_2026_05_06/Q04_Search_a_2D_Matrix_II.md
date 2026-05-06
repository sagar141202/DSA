# Search a 2D Matrix II

## Problem Statement
Write a function to search for a target value in a 2D matrix where each row is sorted in ascending order and each column is sorted in ascending order. The function should return true if the target is found and false otherwise. The matrix can be empty, and the target can be any integer. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
and the target `5`, the function should return `true` because `5` is in the matrix.

## Approach
The algorithm uses a search space reduction approach, starting from the top right corner of the matrix. It compares the target with the current element and moves either left or down based on the comparison. This approach takes advantage of the fact that the rows and columns are sorted.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // Check if the matrix is empty
        if (matrix.size() == 0 || matrix[0].size() == 0) {
            return false;
        }

        int row = 0;
        int col = matrix[0].size() - 1;

        // Continue the search until the row is within the bounds and the column is within the bounds
        while (row < matrix.size() && col >= 0) {
            // If the target is found, return true
            if (matrix[row][col] == target) {
                return true;
            }
            // If the target is less than the current element, move left
            else if (matrix[row][col] > target) {
                col--;
            }
            // If the target is greater than the current element, move down
            else {
                row++;
            }
        }

        // If the target is not found after the search, return false
        return false;
    }
};
```

## Test Cases
```
Input: 
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5
Output: true

Input: 
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 20
Output: false
```

## Key Takeaways
- The search space reduction approach can be applied to problems where the search space can be reduced based on comparisons.
- The time complexity of the solution is O(m + n) because in the worst case, we might need to traverse the entire matrix.
- The space complexity of the solution is O(1) because we only use a constant amount of space to store the row and column indices.