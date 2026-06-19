# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
You are given an array of integers representing the daily stock prices. The task is to find the maximum profit that can be achieved by buying and selling the stock, with the constraint that after selling the stock, you cannot buy it again until a day has passed (i.e., a cooldown period). The stock can be bought and sold any number of times.

## Approach
The problem can be solved using dynamic programming, where we maintain three variables: buy, sell, and cooldown. The buy variable stores the maximum profit when the last action was a buy, the sell variable stores the maximum profit when the last action was a sell, and the cooldown variable stores the maximum profit when the last action was a cooldown.

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
Input: prices = [1,2,3,0,2]
Output: 3
Input: prices = [1]
Output: 0
```

## Key Takeaways
- Use dynamic programming to solve the problem efficiently.
- Maintain three variables (buy, sell, and cooldown) to store the maximum profit at each step.
- The final result is the maximum of the sell and cooldown variables at the last step.