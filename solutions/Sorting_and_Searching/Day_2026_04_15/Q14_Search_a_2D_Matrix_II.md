# Search a 2D Matrix II

## Problem Statement
Write a function that searches for a target value in a 2D matrix where each row is sorted in ascending order and each column is sorted in ascending order. The function should return true if the target is found and false otherwise. The input matrix will have dimensions m x n, where m and n are positive integers. The target value will be an integer.

## Approach
The algorithm starts from the top-right corner of the matrix and moves either left or down based on the comparison of the current element with the target. If the current element is greater than the target, it moves left, and if it is less than the target, it moves down. This approach ensures that the search space is reduced at each step, resulting in an efficient search.

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
        else if (matrix[row][col] > target) col--;
        else row++;
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
- The key to solving this problem is to understand the properties of the input matrix and use them to reduce the search space.
- Starting from the top-right corner and moving either left or down based on the comparison with the target is an efficient approach.
- The time complexity of this solution is O(m + n), where m and n are the dimensions of the matrix, making it efficient for large inputs.