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
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        // Initialize the triangle with the first row
        vector<vector<int>> triangle = {{1}};

        // Generate each row of the triangle
        for (int i = 1; i < numRows; i++) {
            // Initialize the current row with the first element as 1
            vector<int> row = {1};

            // Generate the middle elements of the current row
            for (int j = 1; j < i; j++) {
                // Calculate the sum of the two numbers directly above it
                row.push_back(triangle[i-1][j-1] + triangle[i-1][j]);
            }

            // Add the last element as 1
            row.push_back(1);

            // Add the current row to the triangle
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
- The problem can be solved using dynamic programming.
- The space complexity is O(n^2) because we need to store all the rows of the triangle.
- The time complexity is O(n^2) because we need to generate each element of the triangle.