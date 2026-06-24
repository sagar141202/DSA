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
And the target value is 5, the function should return true. If the target value is 20, the function should return false.

## Approach
We can start from the top right corner of the matrix and compare the target value with the current element. If the target is less than the current element, we move left, otherwise we move down. This approach takes advantage of the fact that the rows and columns are sorted.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int row = 0;
    int col = matrix[0].size() - 1;
    
    while (row < matrix.size() && col >= 0) {
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
Input: 
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Target: 5
Output: true

Input: 
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Target: 20
Output: false
```

## Key Takeaways
- Start from the top right corner of the matrix to take advantage of the sorted rows and columns.
- Compare the target value with the current element and move left or down accordingly.
- The time complexity is O(m + n) because in the worst case we need to traverse all rows and columns.