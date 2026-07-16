# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day. You want to maximize your profit by buying and selling the stock, but you cannot buy the stock on the day after you sell it. The task is to find the maximum possible profit. For example, if the input array is `[1, 2, 3, 0, 2]`, the maximum profit can be achieved by buying on day 0 (price=1), selling on day 2 (price=3), then buying on day 4 (price=0) and selling on day 4 (price=2).

## Approach
The problem can be solved using dynamic programming by maintaining three arrays: `buy`, `sell`, and `cooldown`. The `buy` array stores the maximum profit after buying the stock on each day, the `sell` array stores the maximum profit after selling the stock on each day, and the `cooldown` array stores the maximum profit after cooling down on each day.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n < 2) return 0;
        
        vector<int> buy(n), sell(n), cooldown(n);
        buy[0] = -prices[0];
        sell[0] = 0;
        cooldown[0] = 0;
        
        for (int i = 1; i < n; i++) {
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i]);
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
            cooldown[i] = max(cooldown[i-1], sell[i-1]);
        }
        
        return max(sell[n-1], cooldown[n-1]);
    }
};
```

## Test Cases
```
Input: prices = [1, 2, 3, 0, 2]
Output: 3
Input: prices = [1]
Output: 0
```

## Key Takeaways
- Use dynamic programming to break down the problem into smaller subproblems and store the solutions to subproblems to avoid redundant computation.
- Maintain separate arrays to track the maximum profit after buying, selling, and cooling down on each day.
- The final answer is the maximum of the `sell` and `cooldown` arrays on the last day.