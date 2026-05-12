# Search a 2D Matrix II

## Problem Statement
Write a function that searches for a target value in a 2D matrix, where each row is sorted in ascending order and each column is sorted in ascending order. The function should return true if the target is found, and false otherwise. The matrix can be empty, and the target can be any integer value. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
The target value 5 should return true, and the target value 20 should return false.

## Approach
We can solve this problem by starting from the top right corner of the matrix and moving either left or down based on the comparison of the target with the current element. This approach takes advantage of the fact that the rows and columns are sorted in ascending order. We can repeat this process until we find the target or reach the boundaries of the matrix.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>

class Solution {
public:
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
- The time complexity is O(m + n) because in the worst case, we might need to traverse the entire matrix.
- The space complexity is O(1) because we only use a constant amount of space to store the row and column indices.
- This solution works by taking advantage of the fact that the rows and columns are sorted in ascending order.