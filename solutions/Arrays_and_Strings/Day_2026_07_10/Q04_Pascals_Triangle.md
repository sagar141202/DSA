# Pascal's Triangle

## Problem Statement
Pascal's Triangle is a triangular array of the binomial coefficients. The numbers in Pascal's Triangle can be determined by summing up the two numbers directly above it. Given an integer `numRows`, return the first `numRows` of Pascal's triangle. For example, if `numRows` is 5, the output should be `[[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]`. The input `numRows` will be in the range [1, 30].

## Approach
The algorithm uses dynamic programming to generate each row of Pascal's Triangle. It starts with the first row as `[1]` and then generates each subsequent row by summing adjacent elements from the previous row. The process is repeated until the desired number of rows is reached.

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
        
        // Generate each row
        for (int i = 1; i < numRows; i++) {
            vector<int> row = {1};
            // Calculate the middle elements
            for (int j = 1; j < i; j++) {
                row.push_back(triangle[i-1][j-1] + triangle[i-1][j]);
            }
            // Add the last element
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
- The first and last element of each row is always 1.
- Each element in the triangle is the sum of the two elements directly above it.
- The use of dynamic programming allows for efficient generation of Pascal's Triangle.