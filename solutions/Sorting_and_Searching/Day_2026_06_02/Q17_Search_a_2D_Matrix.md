# Search a 2D Matrix

## Problem Statement
Write a function that searches for a target value in a 2D matrix, where each row is sorted in ascending order and each column is sorted in ascending order. The function should return the coordinates (row, column) of the target value if found, or (-1, -1) if not found. The input matrix is a 2D vector of integers, and the target value is an integer. For example, given the matrix:
```
[
  [1, 4, 7, 11, 15],
  [2, 5, 8, 12, 19],
  [3, 6, 9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
and the target value 5, the function should return (1, 1).

## Approach
The algorithm starts from the top-right corner of the matrix and compares the target value with the current element. If the target value is less than the current element, it moves left; otherwise, it moves down. This process continues until the target value is found or the search space is exhausted.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return {-1, -1};
        
        int row = 0, col = matrix[0].size() - 1;
        while (row < matrix.size() && col >= 0) {
            if (matrix[row][col] == target) return {row, col};
            else if (matrix[row][col] > target) col--;
            else row++;
        }
        return {-1, -1};
    }
};
```

## Test Cases
```
Input: matrix = [
  [1, 4, 7, 11, 15],
  [2, 5, 8, 12, 19],
  [3, 6, 9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], target = 5
Output: [1, 1]
```

## Key Takeaways
- Start from the top-right corner of the matrix to take advantage of the sorted rows and columns.
- Use a while loop to iterate through the matrix, moving left or down based on the comparison with the target value.
- Return the coordinates of the target value if found, or (-1, -1) if not found.