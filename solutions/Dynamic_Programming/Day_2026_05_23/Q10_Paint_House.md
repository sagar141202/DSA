# Paint House

## Problem Statement
There are a row of houses, each house can be painted with three colors: red, blue and green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color. The cost of painting each house with a certain color is given. You need to find the minimum cost to paint all the houses.

## Approach
The problem can be solved using dynamic programming. We can create a 2D array where each cell represents the minimum cost to paint the houses up to that point with a certain color. We can then fill up this array by considering the minimum cost to paint the previous house with a different color.

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
    vector<vector<int>> dp(n, vector<int>(3, 0));
    dp[0][0] = costs[0][0];
    dp[0][1] = costs[0][1];
    dp[0][2] = costs[0][2];
    for (int i = 1; i < n; i++) {
        dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2]);
        dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2]);
        dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1]);
    }
    return min(min(dp[n-1][0], dp[n-1][1]), dp[n-1][2]);
}

int main() {
    vector<vector<int>> costs = {{17,2,17},{16,16,5},{14,3,19}};
    cout << minCost(costs) << endl;
    return 0;
}
```

## Test Cases
```
Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
```

## Key Takeaways
- Use dynamic programming to solve the problem.
- The time complexity is linear, which makes it efficient for large inputs.
- The space complexity is also linear, which makes it suitable for large inputs.