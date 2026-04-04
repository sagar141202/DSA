# Search a 2D Matrix II

## Problem Statement
Write a function that searches for a target value in a 2D matrix where each row is sorted in ascending order and each column is sorted in ascending order. The function should return true if the target is found, and false otherwise. The matrix can be empty, and the target can be any integer.

## Approach
The algorithm starts from the top right corner of the matrix and moves either left or down depending on whether the target is less than or greater than the current element. This approach takes advantage of the fact that the matrix is sorted in both rows and columns.

## Complexity
- Time: O(m + n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    // Check if the matrix is empty
    if (matrix.size() == 0 || matrix[0].size() == 0) {
        return false;
    }

    // Initialize the row and column pointers
    int row = 0;
    int col = matrix[0].size() - 1;

    // Search for the target
    while (row < matrix.size() && col >= 0) {
        if (matrix[row][col] == target) {
            return true;
        } else if (matrix[row][col] > target) {
            // Move left if the target is less than the current element
            col--;
        } else {
            // Move down if the target is greater than the current element
            row++;
        }
    }

    // Return false if the target is not found
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
- The time complexity of the solution is O(m + n), where m is the number of rows and n is the number of columns in the matrix.
- The space complexity of the solution is O(1), as it only uses a constant amount of space to store the row and column pointers.
- The solution takes advantage of the fact that the matrix is sorted in both rows and columns, allowing it to efficiently search for the target value.