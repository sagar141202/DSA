# Pascal's Triangle

## Problem Statement
Pascal's Triangle is a triangular array of the binomial coefficients where each number is the number of combinations of a certain size that can be selected from a set of items. The problem requires generating the first 'n' rows of Pascal's Triangle. The input is an integer 'n' representing the number of rows, and the output is a 2D array representing the first 'n' rows of Pascal's Triangle. The constraints are 1 <= n <= 30.

## Approach
The algorithm uses dynamic programming to generate each row based on the previous row. The first and last element of each row is always 1, and the other elements are the sum of the two elements directly above it in the previous row.

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
        vector<vector<int>> triangle(numRows);
        for (int i = 0; i < numRows; i++) {
            triangle[i].resize(i + 1, 1);
            for (int j = 1; j < i; j++) {
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j];
            }
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
- The first and last element of each row in Pascal's Triangle is always 1.
- Each element in Pascal's Triangle is the sum of the two elements directly above it in the previous row.
- The problem can be solved using dynamic programming, where each row is generated based on the previous row.