# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
You are given an array of integers representing the daily prices of a stock. You can buy and sell the stock, but you must wait at least one day after selling before buying again. The goal is to find the maximum profit that can be achieved. The constraints are: 1 <= prices.length <= 5000, 0 <= prices[i] <= 10^5. For example, if the input is [1, 2, 3, 0, 2], the output should be 3.

## Approach
The problem can be solved using dynamic programming, where we maintain three variables: buy, sell, and cooldown. The buy variable represents the maximum profit after buying the stock, the sell variable represents the maximum profit after selling the stock, and the cooldown variable represents the maximum profit after cooling down. We update these variables iteratively based on the current price.

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
        
        // Initialize variables
        vector<int> buy(n), sell(n), cooldown(n);
        buy[0] = -prices[0];
        sell[0] = 0;
        cooldown[0] = 0;
        
        // Update variables iteratively
        for (int i = 1; i < n; i++) {
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i]);
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
            cooldown[i] = max(cooldown[i-1], sell[i-1]);
        }
        
        // Return the maximum profit
        return sell[n-1];
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
- We use dynamic programming to solve the problem efficiently.
- We maintain three variables: buy, sell, and cooldown, to keep track of the maximum profit at each step.
- The final result is stored in the sell variable at the last index.