# Pascal's Triangle

## Problem Statement
Pascal's Triangle is a triangular array of the binomial coefficients where each number is the number of combinations of a certain size that can be selected from a set of items. The problem requires generating the first 'n' rows of Pascal's triangle. The first row is 1, the second row is 1 1, the third row is 1 2 1, and so on. The value of each cell can be calculated as the sum of the two numbers directly above it. The constraints are 1 <= n <= 30.

## Approach
The algorithm generates each row of Pascal's triangle iteratively, starting with the first row as 1. For each subsequent row, it calculates the values as the sum of the two numbers directly above it. This approach ensures that the triangle is generated row by row.

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
Output: [
         [1],
         [1,1],
         [1,2,1],
         [1,3,3,1],
         [1,4,6,4,1]
        ]
```

## Key Takeaways
- The problem can be solved using dynamic programming by generating each row based on the previous row.
- The time complexity is O(n^2) because we are generating 'n' rows and each row has up to 'n' elements.
- The space complexity is also O(n^2) because we need to store all the elements of the triangle.