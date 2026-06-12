# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
You are given an array of integers representing the prices of a stock over time. The goal is to find the maximum profit that can be achieved by buying and selling the stock, subject to the constraint that you cannot buy a stock on the day after selling a stock. In other words, after selling a stock, you must wait at least one day before buying another stock. The array of prices is non-empty, and all prices are non-negative. For example, if the input array is [1, 2, 3, 0, 2], the maximum profit is 3, which can be achieved by buying at price 1, selling at price 3, waiting one day, and then buying at price 0 and selling at price 2.

## Approach
The problem can be solved using dynamic programming by maintaining three variables: buy, sell, and cooldown. The buy variable stores the maximum profit after buying a stock, the sell variable stores the maximum profit after selling a stock, and the cooldown variable stores the maximum profit after a cooldown period. The algorithm iterates over the array of prices, updating these variables at each step.

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
Input: [1, 2, 3, 0, 2]
Output: 3
```

## Key Takeaways
- The dynamic programming approach is suitable for problems with overlapping subproblems and optimal substructure.
- The use of three variables (buy, sell, and cooldown) allows us to keep track of the maximum profit at each step, considering the cooldown constraint.
- The time complexity is linear, making the solution efficient for large inputs.