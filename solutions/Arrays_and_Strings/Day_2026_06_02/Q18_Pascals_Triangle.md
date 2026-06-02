# Pascal's Triangle

## Problem Statement
Pascal's Triangle is a triangular array of the binomial coefficients where each number is the number of combinations of a certain size that can be selected from a set of items. The problem requires generating the first 'numRows' of Pascal's Triangle. For example, given numRows = 5, the output should be [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]. The constraints are 1 <= numRows <= 30.

## Approach
The algorithm uses dynamic programming to generate each row of Pascal's Triangle. Each element in a row is the sum of the two elements directly above it in the previous row. The first and last elements of each row are always 1.

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
Input: numRows = 5
Output: [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
```

## Key Takeaways
- The problem can be solved using dynamic programming by generating each row based on the previous row.
- The time complexity is O(n^2) because we are generating 'n' rows and each row has up to 'n' elements.
- The space complexity is O(n^2) because we are storing all the rows in the result.