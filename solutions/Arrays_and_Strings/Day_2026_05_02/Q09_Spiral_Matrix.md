# Spiral Matrix

## Problem Statement
Given an integer `n`, generate a spiral matrix of size `n x n` where the numbers are filled in a spiral order, starting from 1 and ending at `n * n`. The spiral should start from the top left corner and move clockwise. For example, given `n = 3`, the output should be:
```
1 2 3
8 9 4
7 6 5
```
The constraints are `1 <= n <= 20` and the input will always be a positive integer.

## Approach
The algorithm will use four pointers to track the current boundaries of the matrix and fill the numbers in a spiral order. It will start by filling the first row, then the last column, then the last row, and finally the first column.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<vector<int>> generateMatrix(int n) {
    vector<vector<int>> matrix(n, vector<int>(n, 0));
    int top = 0, bottom = n - 1, left = 0, right = n - 1;
    int num = 1;
    while (top <= bottom && left <= right) {
        // fill the first row
        for (int i = left; i <= right; i++) {
            matrix[top][i] = num++;
        }
        top++;
        
        // fill the last column
        for (int i = top; i <= bottom; i++) {
            matrix[i][right] = num++;
        }
        right--;
        
        // fill the last row
        if (top <= bottom) {
            for (int i = right; i >= left; i--) {
                matrix[bottom][i] = num++;
            }
            bottom--;
        }
        
        // fill the first column
        if (left <= right) {
            for (int i = bottom; i >= top; i--) {
                matrix[i][left] = num++;
            }
            left++;
        }
    }
    return matrix;
}
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
- Use four pointers to track the current boundaries of the matrix.
- Fill the numbers in a spiral order by iterating over the rows and columns.
- Use a counter to keep track of the current number to be filled in the matrix.