# Pascal's Triangle

## Problem Statement
Pascal's Triangle is a triangular array of the binomial coefficients. The numbers in Pascal's Triangle can be determined by summing up the two numbers directly above it. Given an integer `numRows`, return the first `numRows` of Pascal's triangle. For example, if `numRows` is 5, the output should be `[[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]`. The constraints are `1 <= numRows <= 30`.

## Approach
The approach is to generate each row of Pascal's Triangle iteratively, starting from the second row. Each element in a row is the sum of the two elements directly above it in the previous row.

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
        // Initialize the first row
        triangle.push_back({1});
        
        // Generate each row from the second row to the nth row
        for (int i = 1; i < numRows; i++) {
            vector<int> row = {1};
            // Calculate each element in the current row
            for (int j = 1; j < i; j++) {
                row.push_back(triangle[i-1][j-1] + triangle[i-1][j]);
            }
            row.push_back(1);
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
```

## Key Takeaways
- The first and last elements of each row in Pascal's Triangle are always 1.
- Each element in a row is the sum of the two elements directly above it in the previous row.
- The time complexity of generating Pascal's Triangle up to the nth row is O(n^2), where n is the number of rows.