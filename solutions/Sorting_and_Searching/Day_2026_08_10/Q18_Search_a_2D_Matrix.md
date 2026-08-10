# Search a 2D Matrix

## Problem Statement
Given a 2D matrix of integers `matrix` and an integer `target`, search for the `target` in the 2D matrix. The matrix has the following properties: 
- The matrix is sorted in ascending order from left to right and top to bottom.
- Each row in the matrix is sorted in ascending order from left to right.
- The matrix does not contain duplicate elements.
The function should return `true` if the `target` is found in the matrix, and `false` otherwise.

## Approach
We can treat the 2D matrix as a 1D sorted array and use binary search to find the target. We map the 2D coordinates to a 1D index using the formula `index = row * cols + col`, where `row` is the current row, `cols` is the number of columns, and `col` is the current column.

## Complexity
- Time: O(log(m * n))
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // Get the number of rows and columns
        int rows = matrix.size();
        int cols = matrix[0].size();
        
        // Initialize the low and high pointers for binary search
        int low = 0;
        int high = rows * cols - 1;
        
        // Perform binary search
        while (low <= high) {
            // Calculate the mid index
            int mid = low + (high - low) / 2;
            
            // Map the 1D index to 2D coordinates
            int midRow = mid / cols;
            int midCol = mid % cols;
            
            // Compare the middle element with the target
            if (matrix[midRow][midCol] == target) {
                return true;
            } else if (matrix[midRow][midCol] < target) {
                // If the middle element is less than the target, move to the right half
                low = mid + 1;
            } else {
                // If the middle element is greater than the target, move to the left half
                high = mid - 1;
            }
        }
        
        // If the target is not found, return false
        return false;
    }
};
```

## Test Cases
```
Input: matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
], target = 3
Output: true

Input: matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
], target = 13
Output: false
```

## Key Takeaways
- The problem can be solved by treating the 2D matrix as a 1D sorted array.
- Binary search can be used to find the target in the sorted array.
- The 1D index can be mapped to 2D coordinates using the formula `index = row * cols + col`.