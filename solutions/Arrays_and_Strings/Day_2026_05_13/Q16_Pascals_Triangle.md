# Pascal's Triangle

## Problem Statement
Pascal's Triangle is a triangular array of the binomial coefficients. The numbers in Pascal's Triangle can be determined by summing up the two numbers directly above it. Given an integer `numRows`, return the first `numRows` of Pascal's triangle. For example, if `numRows` is 5, the output should be `[ [1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1] ]`. The constraints are `1 <= numRows <= 30`.

## Approach
The algorithm generates each row of Pascal's Triangle by iterating over the previous row and summing adjacent elements. The first and last elements of each row are always 1.

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
            vector<int> row(i + 1, 1);
            for (int j = 1; j < i; j++) {
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
            }
            triangle.push_back(row);
        }
        return triangle;
    }
};
```

## Test Cases
```
Input: numRows = 5
Output: [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
```

## Key Takeaways
- Initialize the first row of Pascal's Triangle with a single element, 1.
- Generate each subsequent row by summing adjacent elements from the previous row.
- The first and last elements of each row are always 1, which serves as the base case for the recursive formula.