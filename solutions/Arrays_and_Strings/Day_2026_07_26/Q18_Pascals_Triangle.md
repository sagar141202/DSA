# Pascal's Triangle

## Problem Statement
Pascal's Triangle is a triangular array of the binomial coefficients. The numbers in Pascal's Triangle can be determined by summing up the two numbers directly above it. Given an integer `numRows`, return the first `numRows` of Pascal's Triangle. For example, if `numRows` is 5, the output should be `[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]`. The constraints are `1 <= numRows <= 30`.

## Approach
The algorithm uses dynamic programming to generate each row of Pascal's Triangle. It starts with the first row as `[1]` and then generates each subsequent row by summing up the two numbers directly above it. The process continues until the desired number of rows is reached. The time complexity is optimized by only storing the previous row.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> triangle;
        triangle.push_back({1});
        
        for (int i = 1; i < numRows; i++) {
            vector<int> row = {1};
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
Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

## Key Takeaways
- The problem can be solved using dynamic programming.
- The space complexity can be optimized by only storing the previous row.
- The time complexity is quadratic due to the nested loops.