# Triangle Minimum Path

## Problem Statement
Given a triangle array where each row represents a level in the triangle, find the minimum path sum from the top to the bottom. Each step, you may move to an adjacent number in the row below. The triangle array is represented as a 2D array, where the i-th row has i+1 elements. For example, given the triangle `[[2], [3,4], [6,5,7], [4,1,8,3]]`, the minimum path sum from the top to the bottom is `2 + 3 + 5 + 1 = 11`. The constraints are that the input triangle will have at least one row and at most 200 rows, and each number in the triangle will be between 0 and 999.

## Approach
We can solve this problem using dynamic programming, by maintaining an array of minimum path sums at each level. We start from the second last row and move upwards, updating the minimum path sum at each position. The minimum path sum at each position is the minimum of the path sums of its two adjacent numbers in the row below, plus the current number.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<vector<int>> dp(n);
        for (int i = 0; i < n; i++) {
            dp[i].resize(i + 1);
        }
        
        // Initialize the last row of dp
        for (int i = 0; i < n; i++) {
            dp[n - 1][i] = triangle[n - 1][i];
        }
        
        // Fill up the dp table in a bottom-up manner
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j <= i; j++) {
                dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1]);
            }
        }
        
        // The minimum path sum is stored in dp[0][0]
        return dp[0][0];
    }
};

int main() {
    Solution solution;
    vector<vector<int>> triangle = {{2}, {3, 4}, {6, 5, 7}, {4, 1, 8, 3}};
    cout << solution.minimumTotal(triangle) << endl;
    return 0;
}
```

## Test Cases
```
Input: [[2], [3,4], [6,5,7], [4,1,8,3]]
Output: 11
```

## Key Takeaways
- Use dynamic programming to maintain an array of minimum path sums at each level.
- Start from the second last row and move upwards to fill up the dp table.
- The minimum path sum at each position is the minimum of the path sums of its two adjacent numbers in the row below, plus the current number.