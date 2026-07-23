# Pascal's Triangle

## Problem Statement
Pascal's Triangle is a triangular array of the binomial coefficients where each number is the number of combinations of a certain size that can be selected from a set of items. The problem requires generating the first 'n' rows of Pascal's Triangle. The first row is always [1], the second row is always [1, 1], and each subsequent row is formed by adding the two numbers above it to form a new number. The constraints are 1 <= n <= 30.

## Approach
The algorithm involves initializing the first row of Pascal's Triangle as [1] and then iteratively generating each subsequent row by adding the two numbers above it. This process is repeated 'n' times to generate the first 'n' rows of the triangle.

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
        vector<int> first_row = {1};
        triangle.push_back(first_row);
        
        for (int i = 1; i < numRows; i++) {
            vector<int> row = {1};
            vector<int> last_row = triangle[i - 1];
            
            for (int j = 1; j < i; j++) {
                row.push_back(last_row[j - 1] + last_row[j]);
            }
            
            row.push_back(1);
            triangle.push_back(row);
        }
        
        return triangle;
    }
};

int main() {
    Solution solution;
    int numRows = 5;
    vector<vector<int>> result = solution.generate(numRows);
    
    for (const auto& row : result) {
        for (int num : row) {
            cout << num << " ";
        }
        cout << endl;
    }
    
    return 0;
}
```

## Test Cases
```
Input: numRows = 5
Output:
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
```

## Key Takeaways
- The first and last elements of each row in Pascal's Triangle are always 1.
- Each element in Pascal's Triangle is the sum of the two elements directly above it.
- The number of rows in Pascal's Triangle is determined by the input 'n'.