# Search a 2D Matrix

## Problem Statement
Write a function that searches for a target value in a 2D matrix. The matrix is sorted in ascending order from left to right and top to bottom. The function should return `true` if the target is found and `false` otherwise. The matrix is not empty and does not contain empty rows. For example, given the following matrix:
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
We can use a binary search approach to find the target in the 2D matrix, treating it as a 1D sorted array. We start from the top right corner and move left if the target is smaller, or down if the target is larger.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        int row = 0;
        int col = n - 1;
        
        while (row < m && col >= 0) {
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
- We can treat a 2D sorted matrix as a 1D sorted array to apply binary search.
- Starting from the top right corner allows us to move either left or down based on the comparison with the target.
- The time complexity is O(m + n) because in the worst case, we might need to traverse the entire matrix.