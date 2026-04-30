# Pascal's Triangle

## Problem Statement
Pascal's Triangle is a triangular array of the binomial coefficients. The numbers in Pascal's Triangle can be determined by summing up the two numbers directly above it. Given an integer `numRows`, return the first `numRows` of Pascal's triangle. For example, if `numRows` is 5, the output should be `[ [1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1] ]`. The input `numRows` will be in the range `[1, 30]`.

## Approach
The algorithm starts by initializing the first row of Pascal's triangle as `[1]`. Then, it iteratively generates each subsequent row by summing adjacent elements from the previous row. This process continues until the desired number of rows is reached.

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
        triangle.push_back({1});
        
        for (int i = 1; i < numRows; i++) {
            vector<int> row = {1};
            vector<int> lastRow = triangle[i-1];
            
            for (int j = 1; j < i; j++) {
                row.push_back(lastRow[j-1] + lastRow[j]);
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
Input: 1
Output: [[1]]
```

## Key Takeaways
- The first and last element of each row in Pascal's triangle is always 1.
- Each element in Pascal's triangle is the sum of the two elements directly above it.
- The `numRows` parameter determines the number of rows to generate in Pascal's triangle.