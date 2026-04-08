# Pascal's Triangle

## Problem Statement
Pascal's Triangle is a triangular array of the binomial coefficients, where each number is the number of combinations of a certain size that can be selected from a set of items. The first row is 1, the second row is 1 1, the third row is 1 2 1, and so on. The task is to generate the first n rows of Pascal's Triangle, where n is a given integer. For example, if n = 5, the output should be [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]].

## Approach
The algorithm uses dynamic programming to generate each row of Pascal's Triangle. It starts with the first row as [1] and then generates each subsequent row by adding the two numbers directly above it in the previous row.

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
Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

## Key Takeaways
- The solution uses a dynamic programming approach to generate each row of Pascal's Triangle.
- The time complexity is O(n^2) because we are generating n rows, and each row takes O(n) time to generate.
- The space complexity is O(n^2) because we are storing all the rows in the triangle.