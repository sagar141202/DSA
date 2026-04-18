# Paint House

## Problem Statement
There are a row of houses, each house can be painted with three colors: red, blue and green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color. The cost of painting each house with a certain color is given by a 2D array where costs[i][j] is the cost of painting the ith house with the jth color. The goal is to find the minimum cost to paint all the houses.

## Approach
The problem can be solved using dynamic programming by maintaining the minimum cost of painting the current house with each color. We can use a 2D array dp where dp[i][j] represents the minimum cost of painting the first i houses such that the ith house is painted with the jth color.

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
            dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2]);
            dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2]);
            dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1]);
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
- Use dynamic programming to solve the problem by maintaining the minimum cost of painting the current house with each color.
- Initialize the dp array with the costs of painting the first house with each color.
- Fill up the dp array by iterating through the houses and updating the minimum cost of painting the current house with each color based on the minimum cost of painting the previous house with the other two colors.