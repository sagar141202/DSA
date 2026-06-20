# Spiral Matrix

## Problem Statement
Given a matrix of size m x n, generate a spiral matrix. A spiral matrix is a matrix filled with numbers in a spiral pattern, starting from the top left and moving clockwise. The input will be the number of rows (m) and columns (n), and the output will be a 2D vector representing the spiral matrix. For example, if m = 3 and n = 4, the output should be:
```
[
 [1, 2, 3, 4],
 [10, 11, 12, 5],
 [9, 8, 7, 6]
]
```
The constraints are 1 <= m <= 10^3, 1 <= n <= 10^3.

## Approach
The algorithm will start from the top left and fill the matrix in a spiral pattern by maintaining four pointers (top, bottom, left, right) to track the current boundaries of the matrix. It will then move the pointers accordingly to fill the matrix.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> generateMatrix(int m, int n) {
    vector<vector<int>> matrix(m, vector<int>(n, 0));
    int top = 0, bottom = m - 1, left = 0, right = n - 1;
    int num = 1;
    
    while (top <= bottom && left <= right) {
        // Fill the top row
        for (int i = left; i <= right; i++) {
            matrix[top][i] = num++;
        }
        top++;
        
        // Fill the right column
        for (int i = top; i <= bottom; i++) {
            matrix[i][right] = num++;
        }
        right--;
        
        // Fill the bottom row
        if (top <= bottom) {
            for (int i = right; i >= left; i--) {
                matrix[bottom][i] = num++;
            }
            bottom--;
        }
        
        // Fill the left column
        if (left <= right) {
            for (int i = bottom; i >= top; i--) {
                matrix[i][left] = num++;
            }
            left++;
        }
    }
    
    return matrix;
}

int main() {
    int m = 3, n = 4;
    vector<vector<int>> matrix = generateMatrix(m, n);
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
    
    return 0;
}
```

## Test Cases
```
Input: m = 3, n = 4
Output: 
1 2 3 4 
10 11 12 5 
9 8 7 6 
```

## Key Takeaways
- The spiral matrix is filled by maintaining four pointers to track the current boundaries of the matrix.
- The algorithm starts from the top left and moves clockwise to fill the matrix.
- The time complexity is O(m*n) and the space complexity is O(m*n) as we are filling the entire matrix.