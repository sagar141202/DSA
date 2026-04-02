# Search a 2D Matrix

## Problem Statement
Write a function to search for a target element in a 2D matrix, where each row is sorted in ascending order and each column is also sorted in ascending order. The function should take as input a 2D matrix and a target element, and return true if the target element is found in the matrix, and false otherwise. The matrix can be empty, and the target element can be any integer. For example, given the matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
and the target element 5, the function should return true because 5 is in the matrix.

## Approach
The algorithm starts from the top-right corner of the matrix and compares the target element with the current element. If the target element is less than the current element, it moves left, otherwise it moves down. This approach takes advantage of the fact that the rows and columns are sorted.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;
        
        int m = matrix.size();
        int n = matrix[0].size();
        
        int row = 0;
        int col = n - 1;
        
        while (row < m && col >= 0) {
            if (matrix[row][col] == target) return true;
            else if (matrix[row][col] < target) row++;
            else col--;
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
- Start from the top-right corner of the matrix to take advantage of the sorted rows and columns.
- Move left if the target element is less than the current element, otherwise move down.
- The time complexity is O(m + n) because in the worst case, we need to traverse the entire matrix.