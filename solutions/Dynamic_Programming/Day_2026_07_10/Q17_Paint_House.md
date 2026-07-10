# Paint House

## Problem Statement
There are a row of houses, each house can be painted with three colors: red, blue and green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color. The cost of painting each house with a certain color is given. Find the minimum cost to paint all houses.

## Approach
We will use dynamic programming to solve this problem, where we maintain a 2D array `dp` where `dp[i][j]` represents the minimum cost to paint the first `i` houses with the `i-th` house painted with color `j`. We will fill up this array iteratively.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        if (costs.empty()) return 0;
        int n = costs.size();
        vector<vector<int>> dp(n, vector<int>(3, 0));
        dp[0] = costs[0];
        for (int i = 1; i < n; i++) {
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0];
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1];
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2];
        }
        return min({dp[n-1][0], dp[n-1][1], dp[n-1][2]});
    }
};
```

## Test Cases
```
Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems.
- The `dp` array should be filled up iteratively, using the previously computed values to compute the next ones.
- The base case should be handled carefully, in this case, the first row of the `dp` array is initialized with the costs of the first house.