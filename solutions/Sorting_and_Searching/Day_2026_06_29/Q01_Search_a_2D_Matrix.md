# Search a 2D Matrix

## Problem Statement
Write a function to search for a target value in a 2D matrix where each row is sorted in ascending order and each column is sorted in ascending order. The function should return true if the target is found, and false otherwise. The matrix can be of any size, and the target can be any integer. For example, given the matrix:
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
The algorithm starts from the top right corner of the matrix and compares the target with the current element. If the target is less than the current element, it moves left; otherwise, it moves down. This approach ensures that the target is found if it exists in the matrix. The algorithm runs in O(m + n) time, where m and n are the number of rows and columns in the matrix.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // start from the top right corner
        int row = 0, col = matrix[0].size() - 1;
        
        // continue searching while the current position is within the matrix
        while (row < matrix.size() && col >= 0) {
            // if the target is found, return true
            if (matrix[row][col] == target) {
                return true;
            }
            // if the target is less than the current element, move left
            else if (matrix[row][col] > target) {
                col--;
            }
            // if the target is greater than the current element, move down
            else {
                row++;
            }
        }
        // if the target is not found, return false
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
- The algorithm takes advantage of the fact that each row and column is sorted in ascending order.
- The time complexity is O(m + n) because in the worst case, the algorithm needs to traverse the entire matrix.
- The space complexity is O(1) because the algorithm only uses a constant amount of space to store the current position and the target.