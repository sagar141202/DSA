# Pascal's Triangle

## Problem Statement
Pascal's Triangle is a triangular array of the binomial coefficients. The numbers in Pascal's Triangle can be determined by summing up the two numbers directly above it. Given an integer `numRows`, return the first `numRows` of Pascal's triangle. For example, if `numRows` is 5, the output should be `[ [1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1] ]`. The constraints are `1 <= numRows <= 30`.

## Approach
The algorithm uses dynamic programming to generate each row of Pascal's Triangle. It starts with the first row as `[1]` and then generates each subsequent row by summing up the two numbers directly above it. The process is repeated until the desired number of rows is reached.

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
        // Initialize the result with the first row
        vector<vector<int>> result(1, vector<int>(1, 1));
        
        // Generate each row of Pascal's Triangle
        for (int i = 1; i < numRows; i++) {
            // Initialize the current row with 1
            vector<int> row(i + 1, 0);
            row[0] = 1;
            row[i] = 1;
            
            // Calculate the middle elements of the current row
            for (int j = 1; j < i; j++) {
                row[j] = result[i - 1][j - 1] + result[i - 1][j];
            }
            
            // Add the current row to the result
            result.push_back(row);
        }
        
        return result;
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
- The middle elements of each row can be calculated by summing up the two numbers directly above it.
- Dynamic programming can be used to generate Pascal's Triangle efficiently.