# Paint House

## Problem Statement
There are a row of houses, each house can be painted with three colors: red, blue and green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color. The cost of painting each house with a certain color is given. You need to find the minimum cost to paint all houses.

## Approach
The problem can be solved using dynamic programming, where we maintain three arrays: one for each color, to store the minimum cost of painting the houses up to the current house with the corresponding color. We fill up these arrays iteratively, considering the minimum cost of painting the previous house with the other two colors.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int minCost(vector<vector<int>>& costs) {
    if (costs.empty()) return 0;
    int n = costs.size();
    // base case
    if (n == 1) return min({costs[0][0], costs[0][1], costs[0][2]});
    
    vector<int> dp(n, 0);
    dp[0] = costs[0][0];
    vector<int> dp1(n, 0);
    dp1[0] = costs[0][1];
    vector<int> dp2(n, 0);
    dp2[0] = costs[0][2];
    
    for (int i = 1; i < n; i++) {
        dp[i] = costs[i][0] + min(dp1[i-1], dp2[i-1]);
        dp1[i] = costs[i][1] + min(dp[i-1], dp2[i-1]);
        dp2[i] = costs[i][2] + min(dp[i-1], dp1[i-1]);
    }
    
    return min({dp[n-1], dp1[n-1], dp2[n-1]});
}
```

## Test Cases
```
Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
```

## Key Takeaways
- Use dynamic programming to solve the problem, where we maintain arrays to store the minimum cost of painting the houses up to the current house with the corresponding color.
- Fill up these arrays iteratively, considering the minimum cost of painting the previous house with the other two colors.
- The final answer will be the minimum cost of painting the last house with any of the three colors.