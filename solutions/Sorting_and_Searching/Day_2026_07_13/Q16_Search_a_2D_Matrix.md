# Search a 2D Matrix

## Problem Statement
Given a 2D matrix of integers `matrix` and an integer `target`, search for the `target` in the matrix. The matrix is sorted in a way that all elements in each row are sorted in ascending order and the first element of each row is greater than the last element of the previous row. Return `true` if the `target` is found, otherwise return `false`. The matrix can be empty and can have multiple rows and columns. For example, given `matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]` and `target = 3`, the function should return `true`.

## Approach
We can treat the 2D matrix as a 1D sorted array and use binary search to find the target. The key idea is to map the 2D index to a 1D index. We can calculate the 1D index using the formula `index = row * cols + col`, where `row` is the row index, `cols` is the number of columns, and `col` is the column index.

## Complexity
- Time: O(log(m*n))
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;
        int rows = matrix.size();
        int cols = matrix[0].size();
        int left = 0;
        int right = rows * cols - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int num = matrix[mid / cols][mid % cols];
            if (num == target) return true;
            else if (num < target) left = mid + 1;
            else right = mid - 1;
        }
        return false;
    }
};
```

## Test Cases
```
Input: matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target = 3
Output: true
Input: matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target = 13
Output: false
```

## Key Takeaways
- Treat the 2D matrix as a 1D sorted array to simplify the problem.
- Use binary search to find the target in the sorted array.
- Calculate the 1D index using the formula `index = row * cols + col` to map the 2D index to a 1D index.