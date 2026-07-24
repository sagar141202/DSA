# Search a 2D Matrix II

## Problem Statement
Write a function that searches for a target value in a 2D matrix where each row is sorted in ascending order and each column is sorted in ascending order. The matrix does not have to be a square matrix. The function should return true if the target is found, otherwise return false. The matrix can contain duplicate values and can be empty. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
And the target is 5, the function should return true. If the target is 20, the function should return false.

## Approach
The algorithm starts from the top-right corner of the matrix, then moves left if the target is smaller than the current element, or moves down if the target is larger than the current element. This approach takes advantage of the fact that the rows and columns are sorted.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    if (matrix.empty() || matrix[0].empty()) return false;
    
    int row = 0, col = matrix[0].size() - 1;
    while (row < matrix.size() && col >= 0) {
        if (matrix[row][col] == target) return true;
        else if (matrix[row][col] < target) row++;
        else col--;
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
- Start from the top-right corner to take advantage of the sorted rows and columns.
- Move left or down based on the comparison with the target to reduce the search space.
- The time complexity is O(m + n) because in the worst-case scenario, we might need to traverse the entire matrix.