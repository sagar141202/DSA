# Spiral Matrix

## Problem Statement
Given an integer `n`, generate a spiral matrix of size `n x n` filled with numbers from 1 to `n * n` in a spiral pattern, starting from the top left corner and moving clockwise. The spiral pattern should start with 1 at the top left corner, then move right to `n`, then down to `2 * n`, then left to `3 * n`, and so on, until the entire matrix is filled. For example, given `n = 3`, the output should be:
```
1 2 3
8 9 4
7 6 5
```
Constraints: `1 <= n <= 20`

## Approach
The algorithm uses four pointers to keep track of the current boundaries of the matrix, and fills the matrix in a spiral pattern by iterating over the elements in a clockwise direction. The pointers are updated after each iteration to move the boundaries inward. The algorithm uses a simple and efficient approach to fill the matrix.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## C++ Solution
```cpp
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> generateMatrix(int n) {
        // Initialize the matrix with zeros
        std::vector<std::vector<int>> matrix(n, std::vector<int>(n, 0));
        
        // Initialize the pointers
        int top = 0, bottom = n - 1, left = 0, right = n - 1;
        int num = 1;
        
        // Fill the matrix in a spiral pattern
        while (top <= bottom && left <= right) {
            // Fill the top row from left to right
            for (int i = left; i <= right; i++) {
                matrix[top][i] = num++;
            }
            top++;
            
            // Fill the right column from top to bottom
            for (int i = top; i <= bottom; i++) {
                matrix[i][right] = num++;
            }
            right--;
            
            // Fill the bottom row from right to left
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    matrix[bottom][i] = num++;
                }
                bottom--;
            }
            
            // Fill the left column from bottom to top
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    matrix[i][left] = num++;
                }
                left++;
            }
        }
        
        return matrix;
    }
};
```

## Test Cases
```
Input: n = 3
Output: 
1 2 3
8 9 4
7 6 5

Input: n = 4
Output: 
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
```

## Key Takeaways
- The spiral pattern can be achieved by using four pointers to keep track of the current boundaries of the matrix.
- The algorithm uses a simple and efficient approach to fill the matrix by iterating over the elements in a clockwise direction.
- The time complexity is O(n^2) and the space complexity is O(n^2) due to the matrix.