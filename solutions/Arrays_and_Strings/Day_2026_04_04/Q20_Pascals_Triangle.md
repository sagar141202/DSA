# Pascal's Triangle

## Problem Statement
Pascal's Triangle is a triangular array of the binomial coefficients where each number is the number of combinations of a certain size that can be selected from a set of items. The problem requires generating the first 'n' rows of Pascal's Triangle. The first row is 1, the second row is 1 1, the third row is 1 2 1, and so on. The value at each position in the triangle is the sum of the two numbers directly above it. The constraints are 1 <= n <= 30.

## Approach
The algorithm to generate Pascal's Triangle involves initializing the first row with 1 and then generating each subsequent row based on the previous row. Each element in the new row is the sum of the two elements directly above it in the previous row.

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
- The first and last element of each row is always 1.
- Each element in a row is the sum of the two elements directly above it in the previous row.
- The number of rows 'n' is the input to the problem, and we generate the first 'n' rows of Pascal's Triangle.