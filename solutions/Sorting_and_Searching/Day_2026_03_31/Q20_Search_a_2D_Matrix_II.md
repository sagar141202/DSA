# Search a 2D Matrix II

## Problem Statement
Write an efficient algorithm to search for a target value in a 2D matrix where each row is sorted in ascending order and each column is also sorted in ascending order. The matrix does not have to be a square matrix. The target value can be any integer. If the target is found, return true; otherwise, return false. The matrix can contain duplicate values, and the target value can appear multiple times in the matrix. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
And the target value is 5, the function should return true because 5 exists in the matrix.

## Approach
The algorithm starts from the top-right corner of the matrix. It compares the target value with the current element and moves either left or down based on whether the target is smaller or larger. This approach takes advantage of the fact that the rows and columns are sorted, allowing for an efficient search.

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
- The algorithm's efficiency comes from leveraging the sorted nature of both rows and columns.
- Starting from the top-right corner allows for a simple comparison to decide the direction of the next step.
- The time complexity is linear with respect to the sum of the number of rows and columns, making it efficient for large matrices.