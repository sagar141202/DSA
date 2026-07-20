# Pascal's Triangle

## Problem Statement
Pascal's Triangle is a triangular array of the binomial coefficients where each number is the number of combinations of a certain size that can be selected from a set of items. The problem requires generating the first 'n' rows of Pascal's Triangle. The first row is 1, the second row is 1 1, the third row is 1 2 1, and so on. The value of each cell can be calculated as the sum of the two numbers directly above it. The task is to write a function that takes an integer 'n' as input and returns the first 'n' rows of Pascal's Triangle.

## Approach
The algorithm generates each row of Pascal's Triangle iteratively, starting from the first row. Each row is calculated based on the previous row, where the value of each cell is the sum of the two numbers directly above it. The process continues until 'n' rows have been generated.

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
- The number of elements in each row increases by 1 compared to the previous row.