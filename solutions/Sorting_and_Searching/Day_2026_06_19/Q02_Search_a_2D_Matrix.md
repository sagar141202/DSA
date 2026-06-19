# Search a 2D Matrix

## Problem Statement
Write a function that searches for a target value in a 2D matrix where each row is sorted in ascending order and each column is also sorted in ascending order. The function should return true if the target is found and false otherwise. The matrix is not necessarily a square matrix. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
and the target value is 5, the function should return true because 5 is present in the matrix. If the target value is 20, the function should return false.

## Approach
The algorithm starts from the top right corner of the matrix and compares the target value with the current element. If the target is less than the current element, it moves left; otherwise, it moves down. This approach takes advantage of the fact that the rows and columns are sorted.

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
- The algorithm takes advantage of the fact that the rows and columns are sorted to reduce the search space.
- The time complexity is O(m + n) because in the worst case, the algorithm may need to traverse all rows and columns.
- The space complexity is O(1) because the algorithm only uses a constant amount of space to store the current row and column indices.