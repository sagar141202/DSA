# Search a 2D Matrix

## Problem Statement
Write an efficient algorithm to search for a target element in a 2D matrix that is sorted in a specific way. The matrix has the following properties: each row is sorted in ascending order, and each column is also sorted in ascending order. Given the target element, return its position (row and column indices) if it exists in the matrix, otherwise return [-1, -1]. The matrix is a non-empty list of lists of integers, where each list represents a row in the matrix. The target element is an integer.

## Approach
We start from the top right corner of the matrix and compare the target element with the current element. If the target is smaller, we move left; otherwise, we move down. This approach takes advantage of the sorted properties of the matrix.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> searchMatrix(vector<vector<int>>& matrix, int target) {
        // start from the top right corner
        int row = 0, col = matrix[0].size() - 1;
        while (row < matrix.size() && col >= 0) {
            if (matrix[row][col] == target) {
                // found the target
                return {row, col};
            } else if (matrix[row][col] < target) {
                // target is in the lower rows
                row++;
            } else {
                // target is in the left columns
                col--;
            }
        }
        // target not found
        return {-1, -1};
    }
};
```

## Test Cases
```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: [1,1]
```

## Key Takeaways
- Start from the top right corner to take advantage of the sorted properties of the matrix.
- Move left if the target is smaller than the current element, and move down otherwise.
- The time complexity is O(m + n), where m and n are the number of rows and columns in the matrix, respectively.