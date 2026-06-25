# Spiral Matrix

## Problem Statement
Given a matrix of size m x n, write a function that traverses the matrix in a spiral order (clockwise) and returns the elements in the order they are visited. The function should take as input a 2D vector of integers and return a 1D vector of integers. For example, given the following matrix:
```
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
```
The function should return the vector `[1, 2, 3, 6, 9, 8, 7, 4, 5]`. The matrix can be of any size, and the function should work for all possible inputs.

## Approach
The algorithm uses four pointers to keep track of the current bounds of the matrix. It iterates over the elements in a spiral order by moving the pointers in a clockwise direction. The function continues until all elements have been visited.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> spiralOrder(vector<vector<int>>& matrix) {
    int m = matrix.size();
    if (m == 0) return {};
    int n = matrix[0].size();
    if (n == 0) return {};
    
    vector<int> result;
    int top = 0, bottom = m - 1, left = 0, right = n - 1;
    
    while (top <= bottom && left <= right) {
        // Traverse from left to right
        for (int i = left; i <= right; i++) {
            result.push_back(matrix[top][i]);
        }
        top++;
        
        // Traverse from top to bottom
        for (int i = top; i <= bottom; i++) {
            result.push_back(matrix[i][right]);
        }
        right--;
        
        // Traverse from right to left
        if (top <= bottom) {
            for (int i = right; i >= left; i--) {
                result.push_back(matrix[bottom][i]);
            }
            bottom--;
        }
        
        // Traverse from bottom to top
        if (left <= right) {
            for (int i = bottom; i >= top; i--) {
                result.push_back(matrix[i][left]);
            }
            left++;
        }
    }
    
    return result;
}
```

## Test Cases
```
Input: [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

Input: [
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9,10,11,12]
]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
```

## Key Takeaways
- Use four pointers to keep track of the current bounds of the matrix.
- Iterate over the elements in a spiral order by moving the pointers in a clockwise direction.
- Continue until all elements have been visited.