# Pascal's Triangle

## Problem Statement
Given an integer `numRows`, return the first `numRows` of Pascal's triangle. In Pascal's triangle, each number is the number of combinations of a certain size that can be selected from a set of items. The first row is `1`, the second row is `1 1`, the third row is `1 2 1`, and so on. The `i-th` row of the triangle has `i` numbers, and the `j-th` number in the `i-th` row is the binomial coefficient `i-1` choose `j-1`. For example, if `numRows` is 5, the output should be `[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]`. 

## Approach
To generate Pascal's triangle, we start with the first row as `[1]`. Then, for each subsequent row, we calculate the values as the sum of the two numbers directly above it in the previous row. We use dynamic programming to store and calculate the values of each row.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<vector<int>> generate(int numRows) {
    vector<vector<int>> triangle;
    for (int i = 0; i < numRows; i++) {
        vector<int> row = {1};
        if (!triangle.empty()) {
            vector<int> lastRow = triangle.back();
            for (int j = 0; j < lastRow.size() - 1; j++) {
                row.push_back(lastRow[j] + lastRow[j + 1]);
            }
            row.push_back(1);
        }
        triangle.push_back(row);
    }
    return triangle;
}
```

## Test Cases
```
Input: 5
Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

## Key Takeaways
- The first and last element of each row in Pascal's triangle is always 1.
- Each element in the triangle is the sum of the two elements directly above it.
- Dynamic programming can be used to efficiently generate Pascal's triangle by storing and calculating the values of each row.