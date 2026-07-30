# Search a 2D Matrix

## Problem Statement
Write a function to search for a target element in a 2D matrix that is sorted in a specific way. The matrix is sorted row-wise and column-wise, meaning that for any given row, all elements to the right are greater, and for any given column, all elements below are greater. The function should return `true` if the target element is found, and `false` otherwise. The matrix can be empty, and the target element can be any integer.

## Approach
The algorithm uses a modified binary search approach, starting from the top-right corner of the matrix. It compares the target element with the current element, and if the target is smaller, it moves left, otherwise it moves down. This approach takes advantage of the sorted nature of the matrix.

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
- The time complexity is O(m + n) because in the worst case, we might have to traverse the entire matrix.
- The space complexity is O(1) because we only use a constant amount of space to store the row and column indices.
- The algorithm takes advantage of the sorted nature of the matrix, allowing us to reduce the search space efficiently.