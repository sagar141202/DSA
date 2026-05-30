# Paint House

## Problem Statement
There are a row of houses, each house can be painted with three colors: red, blue and green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color. The cost of painting each house with a certain color is given. You need to find the minimum cost to paint all the houses. The cost of painting the first house with red, blue, and green colors is given as `costs[0][0]`, `costs[0][1]`, and `costs[0][2]` respectively. The cost of painting the `i-th` house with red, blue, and green colors is given as `costs[i][0]`, `costs[i][1]`, and `costs[i][2]` respectively.

## Approach
The problem can be solved using dynamic programming, where we maintain a 2D array `dp` where `dp[i][j]` represents the minimum cost to paint the first `i` houses such that the `i-th` house is painted with the `j-th` color. We can fill up the `dp` array by iterating over the houses and colors, and for each house and color, we consider the minimum cost of painting the previous house with a different color.

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
        vector<vector<int>> dp(n, vector<int>(3));
        dp[0] = costs[0];
        for (int i = 1; i < n; i++) {
            dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2]);
            dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2]);
            dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1]);
        }
        return min({dp[n-1][0], dp[n-1][1], dp[n-1][2]});
    }
};

int main() {
    Solution solution;
    vector<vector<int>> costs = {{17,2,17},{16,16,5},{14,3,19}};
    cout << solution.minCost(costs) << endl;
    return 0;
}
```

## Test Cases
```
Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
```

## Key Takeaways
- We use dynamic programming to solve the problem, which helps us to avoid redundant calculations and improve the efficiency of the solution.
- We maintain a 2D array `dp` to store the minimum cost to paint the first `i` houses such that the `i-th` house is painted with the `j-th` color.
- We fill up the `dp` array by iterating over the houses and colors, and for each house and color, we consider the minimum cost of painting the previous house with a different color.