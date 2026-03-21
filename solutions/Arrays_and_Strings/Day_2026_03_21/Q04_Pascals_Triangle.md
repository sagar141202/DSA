# Pascal's Triangle

## Problem Statement
Pascal's Triangle is a triangular array of the binomial coefficients. The numbers in Pascal's Triangle can be determined by summing up the two numbers directly above it. The first row is 1, the second row is 1 1, the third row is 1 2 1, and so on. Given a non-negative integer numRows, return the first numRows of Pascal's Triangle. For example, if numRows is 5, the output should be [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]. The input is guaranteed to be a non-negative integer.

## Approach
The algorithm uses dynamic programming to generate each row of Pascal's Triangle. It starts with the first row as [1] and then generates each subsequent row by summing up the two numbers directly above it. The process is repeated until the desired number of rows is reached.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<vector<int>> generate(int numRows) {
    // Initialize the result with the first row
    vector<vector<int>> result(1, vector<int>(1, 1));

    // Generate each row of Pascal's Triangle
    for (int i = 1; i < numRows; i++) {
        // Initialize the current row with 1
        vector<int> row(i + 1, 1);

        // Calculate the middle elements of the current row
        for (int j = 1; j < i; j++) {
            row[j] = result[i - 1][j - 1] + result[i - 1][j];
        }

        // Add the current row to the result
        result.push_back(row);
    }

    return result;
}
```

## Test Cases
```
Input: 5
Output: [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
```

## Key Takeaways
- The problem can be solved using dynamic programming by generating each row of Pascal's Triangle iteratively.
- The time complexity is O(n^2) because we need to generate n rows, and each row has up to n elements.
- The space complexity is O(n^2) because we need to store all the elements of Pascal's Triangle.