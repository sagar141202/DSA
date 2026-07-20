# Paint House

## Problem Statement
There are a row of houses, each house can be painted with three colors: red, blue and green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color, and you need to find the minimum cost to paint all the houses. The cost of painting each house with a certain color is given in a 2D array `costs` where `costs[i][0]`, `costs[i][1]`, `costs[i][2]` are the costs of painting the `i-th` house with red, blue and green colors respectively.

## Approach
The problem can be solved using dynamic programming, where we maintain a 2D array `dp` where `dp[i][j]` is the minimum cost to paint the first `i` houses such that the `i-th` house is painted with the `j-th` color. We fill up the `dp` array iteratively and finally return the minimum cost to paint all the houses.

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
        dp[0][0] = costs[0][0];
        dp[0][1] = costs[0][1];
        dp[0][2] = costs[0][2];
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
- Use dynamic programming to solve the problem.
- Maintain a 2D array `dp` to store the minimum cost to paint the first `i` houses such that the `i-th` house is painted with the `j-th` color.
- Fill up the `dp` array iteratively and finally return the minimum cost to paint all the houses.