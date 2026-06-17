# Search a 2D Matrix II

## Problem Statement
Write a function that searches for a target value in a 2D matrix. The matrix is sorted in ascending order from left to right and from top to bottom. The function should return `true` if the target is found and `false` otherwise. The matrix can be empty, and the target can be any integer. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
and a target of `5`, the function should return `true`. If the target is `20`, the function should return `false`.

## Approach
The algorithm starts from the top right corner of the matrix and compares the target with the current element. If the target is less than the current element, it moves left; if the target is greater, it moves down. This approach takes advantage of the sorted nature of the matrix to efficiently search for the target.

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
};
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
- Start from the top right corner of the matrix to take advantage of the sorted nature.
- Compare the target with the current element and move left or down accordingly.
- The algorithm has a time complexity of O(m + n), where m is the number of rows and n is the number of columns.