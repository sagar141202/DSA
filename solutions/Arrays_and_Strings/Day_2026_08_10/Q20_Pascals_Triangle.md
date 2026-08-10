# Pascal's Triangle

## Problem Statement
Pascal's Triangle is a triangular array of the binomial coefficients where each number is the number of combinations of a certain size that can be selected from a set of items. The problem requires generating the first 'n' rows of Pascal's Triangle. The first row is 1, the second row is 1 1, the third row is 1 2 1, and so on. The value at each position in the triangle is the sum of the two numbers directly above it. The function should return a vector of vectors where each inner vector represents a row in the triangle.

## Approach
The solution involves generating each row iteratively, starting from the second row. Each element in a row is calculated as the sum of the two elements directly above it in the previous row. The first and last elements of each row are always 1.

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
        vector<vector<int>> triangle(numRows);
        for (int i = 0; i < numRows; i++) {
            triangle[i].resize(i + 1, 1);
            for (int j = 1; j < i; j++) {
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
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
- The first and last elements of each row are always 1.
- Each element in a row is the sum of the two elements directly above it in the previous row.
- The solution has a time complexity of O(n^2) due to the nested loop structure.