# Paint House

## Problem Statement
There are a row of houses, each house can be painted with three colors: red, blue and green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color. The cost of painting each house with a certain color is given. Find the minimum cost to paint all houses.

## Approach
We can solve this problem using dynamic programming by maintaining the minimum cost of painting the current house with each color. The minimum cost of painting the current house with a certain color is the minimum cost of painting the previous house with a different color plus the cost of painting the current house with the certain color.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int minCost(vector<vector<int>>& costs) {
    if (costs.empty()) return 0;
    int n = costs.size();
    vector<vector<int>> dp(n, vector<int>(3));
    dp[0] = costs[0];
    for (int i = 1; i < n; i++) {
        dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2]);
        dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2]);
        dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1]);
    }
    return min(min(dp[n-1][0], dp[n-1][1]), dp[n-1][2]);
}
```

## Test Cases
```
Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
```

## Key Takeaways
- We use dynamic programming to solve this problem by maintaining the minimum cost of painting the current house with each color.
- The minimum cost of painting the current house with a certain color is the minimum cost of painting the previous house with a different color plus the cost of painting the current house with the certain color.
- The time complexity is O(n) and the space complexity is O(1) if we only consider the space used by the output and the input, otherwise it is O(n).