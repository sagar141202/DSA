# Pascal's Triangle

## Problem Statement
Pascal's Triangle is a triangular array of the binomial coefficients. The numbers in Pascal's Triangle can be determined by summing up the two numbers directly above it. Given a non-negative integer `numRows`, generate the first `numRows` of Pascal's Triangle. For example, if `numRows` is 5, the output should be `[ [1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1] ]`. The constraint is that `numRows` is between 1 and 30.

## Approach
The algorithm is based on the property of Pascal's Triangle where each element is the sum of the two elements directly above it. We start with the first row as `[1]` and then generate each subsequent row by summing adjacent elements from the previous row. This process is repeated `numRows` times to generate the desired output.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## C++ Solution
```cpp
#include <vector>
using namespace std;

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
```

## Test Cases
```
Input: 5
Output: [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
```

## Key Takeaways
- Each row in Pascal's Triangle starts and ends with 1.
- The sum of the elements in the nth row is equal to 2^(n-1).
- The algorithm uses dynamic programming to efficiently generate each row based on the previous row.