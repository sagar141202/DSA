# Pascal's Triangle

## Problem Statement
Pascal's Triangle is a triangular array of the binomial coefficients. The numbers in Pascal's Triangle can be determined by summing up the two numbers directly above it. Given an integer `numRows`, return the first `numRows` of Pascal's Triangle. For example, if `numRows` is 5, the output should be `[ [1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1] ]`. The constraints are `1 <= numRows <= 30`.

## Approach
The algorithm uses dynamic programming to generate each row of Pascal's Triangle based on the previous row. It starts with the first row as `[1]` and then iteratively generates each subsequent row.

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
- The first and last elements of each row in Pascal's Triangle are always 1.
- Each element in Pascal's Triangle is the sum of the two elements directly above it.
- Dynamic programming is used to efficiently generate each row of Pascal's Triangle based on the previous row.