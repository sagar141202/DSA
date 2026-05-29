# Pascal's Triangle

## Problem Statement
Pascal's Triangle is a triangular array of the binomial coefficients. Each number in the triangle is the sum of the two directly above it. The first row is 1, the second row is 1 1, the third row is 1 2 1, and so on. Given a non-negative integer `numRows`, return the first `numRows` of Pascal's triangle. For example, if `numRows` is 5, the output should be `[[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]`. The input `numRows` will be in the range [1, 30].

## Approach
The algorithm uses dynamic programming to generate each row of Pascal's triangle. It starts with the first row as [1] and then generates each subsequent row based on the previous row. The value at each position in the new row is the sum of the two values directly above it in the previous row.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
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
};
```

## Test Cases
```
Input: 5
Output: [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
Input: 1
Output: [[1]]
```

## Key Takeaways
- Use dynamic programming to generate each row of Pascal's triangle based on the previous row.
- The value at each position in the new row is the sum of the two values directly above it in the previous row.
- The time and space complexity of the solution are both O(n^2), where n is the number of rows.