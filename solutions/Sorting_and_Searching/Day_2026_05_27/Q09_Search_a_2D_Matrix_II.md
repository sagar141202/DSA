# Search a 2D Matrix II

## Problem Statement
Write a function that searches for a target value in a 2D matrix where each row is sorted in ascending order and each column is also sorted in ascending order. The function should return `true` if the target is found, and `false` otherwise. The input matrix will have `m` rows and `n` columns, where `m` and `n` are positive integers. The target value will be an integer.

## Approach
The algorithm starts from the top-right corner of the matrix and moves left if the target is smaller than the current element, or moves down if the target is larger. This approach ensures that we can take advantage of the fact that both rows and columns are sorted.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    // start from top-right corner
    int row = 0;
    int col = matrix[0].size() - 1;
    
    // continue search until we are within bounds
    while (row < matrix.size() && col >= 0) {
        // if target is found, return true
        if (matrix[row][col] == target) {
            return true;
        }
        // move left if target is smaller
        else if (matrix[row][col] > target) {
            col--;
        }
        // move down if target is larger
        else {
            row++;
        }
    }
    // if target is not found, return false
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
- Start from the top-right corner to take advantage of the fact that both rows and columns are sorted.
- Move left if the target is smaller than the current element, or move down if the target is larger.
- Continue search until we are within bounds of the matrix.