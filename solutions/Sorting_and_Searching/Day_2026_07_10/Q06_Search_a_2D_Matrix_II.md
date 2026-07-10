# Search a 2D Matrix II

## Problem Statement
Write a function that searches for a target value in a 2D matrix. The matrix has the following properties: 
- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.
The function should return true if the target exists in the matrix, otherwise return false. 
Example:
```
Input: matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5
Output: True
```

## Approach
The algorithm starts from the top-right corner of the matrix and compares the target with the current element. If the target is smaller, it moves left; otherwise, it moves down. This approach takes advantage of the sorted properties of the matrix.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

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
```

## Test Cases
```
Input: matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5
Output: True

Input: matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 20
Output: False
```

## Key Takeaways
- Start from the top-right corner to take advantage of the sorted properties.
- Move left if the target is smaller than the current element, otherwise move down.
- The time complexity is O(m + n) because in the worst-case scenario, we might need to traverse the entire matrix.