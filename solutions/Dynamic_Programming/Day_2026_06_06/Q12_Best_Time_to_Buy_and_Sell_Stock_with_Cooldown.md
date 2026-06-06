# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
You are given an array of integers representing the prices of a stock on different days. You can buy and sell the stock, but you must wait at least one day after selling before buying again. The goal is to find the maximum possible profit. For example, given the prices [1, 2, 3, 0, 2], the maximum profit is 3, which can be achieved by buying on day 0, selling on day 2, and then buying on day 4 and selling on day 4.

## Approach
The problem can be solved using dynamic programming, where we maintain three variables: buy, sell, and cooldown. The buy variable represents the maximum profit after buying the stock, the sell variable represents the maximum profit after selling the stock, and the cooldown variable represents the maximum profit after the cooldown period.

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
        
        // Initialize variables to store the maximum profit
        vector<int> buy(n), sell(n), cooldown(n);
        
        // Base case: buying on the first day
        buy[0] = -prices[0];
        
        // Fill up the dp arrays
        for (int i = 1; i < n; i++) {
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i]);
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
            cooldown[i] = max(cooldown[i-1], sell[i-1]);
        }
        
        // The maximum profit is the maximum of selling and cooldown on the last day
        return max(sell[n-1], cooldown[n-1]);
    }
};
```

## Test Cases
```
Input: [1, 2, 3, 0, 2]
Output: 3
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems.
- Initialize base cases carefully to avoid incorrect results.
- Use meaningful variable names to improve code readability.