# Search a 2D Matrix

## Problem Statement
Given a 2D matrix of integers where each row is sorted in ascending order, search for a target integer. The matrix can be treated as a 1D sorted array where the elements of each row are appended to the previous row. The matrix has `m` rows and `n` columns, and the target integer is `target`. The function should return `true` if the target is found, and `false` otherwise. For example, given the matrix `[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]` and `target = 3`, the function should return `true`. If `target = 13`, the function should return `false`.

## Approach
We can treat the 2D matrix as a 1D sorted array and use binary search to find the target. The key is to map the 1D index to the corresponding 2D index. We can calculate the row and column indices using the formula `row = index / n` and `col = index % n`, where `n` is the number of columns.

## Complexity
- Time: O(log(mn))
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    if (matrix.empty() || matrix[0].empty()) return false;
    int m = matrix.size(), n = matrix[0].size();
    int left = 0, right = m * n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        int num = matrix[mid / n][mid % n];
        if (num == target) return true;
        else if (num < target) left = mid + 1;
        else right = mid - 1;
    }
    return false;
}
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
- Calculate the row and column indices using the formula `row = index / n` and `col = index % n`.