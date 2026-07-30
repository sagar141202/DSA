# Search a 2D Matrix II

## Problem Statement
Write a function that searches for a target value in a 2D matrix. The matrix is sorted in a way that all elements in each row are sorted in ascending order and the first element of each row is greater than the last element of the previous row. The function should return true if the target is found, and false otherwise. The matrix can contain duplicate elements. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
And the target `5`, the function should return `true`.

## Approach
The algorithm uses a modified binary search approach to find the target in the 2D matrix. We start from the top-right corner and move either left or down based on the comparison with the target. This approach takes advantage of the fact that the matrix is sorted in a specific way.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    if (matrix.empty() || matrix[0].empty()) {
        return false;
    }
    
    int row = 0;
    int col = matrix[0].size() - 1;
    
    while (row < matrix.size() && col >= 0) {
        if (matrix[row][col] == target) {
            return true;
        } else if (matrix[row][col] < target) {
            row++;
        } else {
            col--;
        }
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
- The time complexity is O(m + n) where m is the number of rows and n is the number of columns in the matrix.
- The space complexity is O(1) as we only use a constant amount of space to store the row and column indices.
- This solution takes advantage of the fact that the matrix is sorted in a specific way, allowing us to use a modified binary search approach.