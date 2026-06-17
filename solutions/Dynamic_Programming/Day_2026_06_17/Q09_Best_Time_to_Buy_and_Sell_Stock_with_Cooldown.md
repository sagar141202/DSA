# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
Given an array of integers representing the daily stock prices, find the maximum profit that can be achieved by buying and selling the stock with a cooldown period of one day after each sale. The constraints are that you can only hold one stock at a time, and you cannot buy and sell the stock on the same day. For example, if the input array is [1, 2, 3, 0, 2], the maximum profit is 3, which can be achieved by buying on day 0, selling on day 2, and then buying on day 4 and selling on day 4.

## Approach
The algorithm uses dynamic programming to track the maximum profit at each day. It maintains three variables: buy, sell, and cooldown, representing the maximum profit when the last action was a buy, a sell, or a cooldown, respectively. The maximum profit at each day is updated based on the maximum profit of the previous days.

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
        
        // Base case: maximum profit on the first day
        buy[0] = -prices[0];
        sell[0] = 0;
        cooldown[0] = 0;
        
        // Fill up the dp table
        for (int i = 1; i < n; i++) {
            // Maximum profit when the last action was a buy
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i]);
            // Maximum profit when the last action was a sell
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
            // Maximum profit when the last action was a cooldown
            cooldown[i] = max(cooldown[i-1], sell[i-1]);
        }
        
        // The maximum profit is the maximum of sell and cooldown on the last day
        return max(sell[n-1], cooldown[n-1]);
    }
};
```

## Test Cases
```
Input: [1, 2, 3, 0, 2]
Output: 3
Input: [1]
Output: 0
```

## Key Takeaways
- Use dynamic programming to solve the problem efficiently.
- Maintain three variables to track the maximum profit at each day.
- Update the maximum profit at each day based on the maximum profit of the previous days.