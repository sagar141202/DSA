# Pascal's Triangle

## Problem Statement
Pascal's Triangle is a triangular array of the binomial coefficients where each number is the number of combinations of a certain size that can be selected from a set of items. The problem requires generating the first n rows of Pascal's Triangle. The input is an integer n, representing the number of rows. The output should be a vector of vectors, where each inner vector represents a row in the triangle. For example, if n = 5, the output should be [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]].

## Approach
The algorithm uses dynamic programming to generate each row of the triangle based on the previous row. It starts with the first row as [1] and then generates each subsequent row by adding pairs of adjacent numbers from the previous row.

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
- The first and last elements of each row are always 1.
- Each element in the triangle is the sum of the two elements directly above it.
- The number of rows in the triangle is determined by the input parameter n.