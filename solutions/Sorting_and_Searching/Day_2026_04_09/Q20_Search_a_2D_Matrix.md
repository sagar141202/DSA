# Search a 2D Matrix

## Problem Statement
Write a function to search for a target element in a 2D matrix that is sorted in a specific way. The matrix is sorted row-wise and column-wise, meaning that for any element at position (i, j), all elements to its left (i, 0 to j-1) and above it (0 to i-1, j) are smaller than it. The function should take as input the 2D matrix and the target element, and return a boolean indicating whether the target element is present in the matrix or not. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
And the target element `5`, the function should return `true` because `5` is present in the matrix.

## Approach
We can solve this problem by treating the 2D matrix as a 1D sorted array and performing a binary search on it. We start from the top-right corner of the matrix and compare the target element with the current element. If the target element is smaller, we move left; otherwise, we move down.

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

    int rows = matrix.size();
    int cols = matrix[0].size();
    int row = 0;
    int col = cols - 1;

    while (row < rows && col >= 0) {
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
- The key to solving this problem is to treat the 2D matrix as a 1D sorted array.
- We start from the top-right corner of the matrix and compare the target element with the current element.
- We move left if the target element is smaller, and down otherwise.