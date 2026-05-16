# Pascal's Triangle

## Problem Statement
Pascal's Triangle is a triangular array of the binomial coefficients. The numbers in Pascal's Triangle can be determined by summing up the two numbers directly above it. The first row is 1, the second row is 1 1, the third row is 1 2 1, and so on. Given a non-negative integer numRows, return the first numRows of Pascal's triangle. For example, if numRows is 5, the output should be [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]. The constraints are 1 <= numRows <= 30.

## Approach
The algorithm to generate Pascal's Triangle involves initializing the first row as 1 and then iterating over each subsequent row, calculating the values by summing the two numbers directly above it. We use dynamic programming to store the previous row and calculate the next row. The base case is the first row with a single element 1.

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
        // Initialize the result with the first row
        vector<vector<int>> result(1, vector<int>(1, 1));
        
        // Generate each row
        for (int i = 1; i < numRows; i++) {
            // Initialize the current row with 1
            vector<int> row(i + 1, 0);
            row[0] = row[i] = 1;
            
            // Calculate the middle elements of the current row
            for (int j = 1; j < i; j++) {
                row[j] = result[i - 1][j - 1] + result[i - 1][j];
            }
            
            // Add the current row to the result
            result.push_back(row);
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

## Key Takeaways
- Initialize the first row as 1 and use dynamic programming to calculate subsequent rows.
- Each element in a row is the sum of the two elements directly above it in the previous row.
- The time complexity is O(n^2) and the space complexity is O(n^2) due to the storage of the entire triangle.