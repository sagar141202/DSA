# Search a 2D Matrix II

## Problem Statement
Write a function that searches for a target value in a 2D matrix where each row is sorted in ascending order and each column is also sorted in ascending order. The function should return `true` if the target is found and `false` otherwise. The matrix can be empty, and the target can be any integer. For example, given the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
and target `5`, the function should return `true` because `5` is in the matrix.

## Approach
The algorithm starts from the top-right corner of the matrix and moves either left or down based on the comparison between the current element and the target. This approach takes advantage of the fact that the rows and columns are sorted. By moving left if the current element is greater than the target and moving down if the current element is less than the target, we can efficiently search for the target in the matrix.

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
- The key to solving this problem efficiently is to take advantage of the fact that both rows and columns are sorted.
- Starting from the top-right corner allows us to make decisions based on the comparison with the target, effectively reducing the search space with each move.
- This approach results in a time complexity of O(m + n), where m is the number of rows and n is the number of columns, because in the worst case, we might have to traverse through all rows and columns.