# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
You are given an array of integers representing the prices of a stock on different days. You can buy and sell the stock, but you must wait at least one day after selling before buying again. The goal is to find the maximum profit that can be achieved. The prices array will have at least one element, and all elements will be non-negative integers. For example, if the input is [1, 2, 3, 0, 2], the output should be 3, because you can buy on day 0, sell on day 2, and then buy on day 4 and sell on day 4.

## Approach
The problem can be solved using dynamic programming by maintaining three variables: buy, sell, and cooldown. The buy variable stores the maximum profit after buying the stock, the sell variable stores the maximum profit after selling the stock, and the cooldown variable stores the maximum profit after the cooldown period. The algorithm iterates through the prices array, updating these variables at each step.

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
        
        // Base cases
        buy[0] = -prices[0];
        sell[0] = 0;
        cooldown[0] = 0;
        
        // Fill up the tables
        for (int i = 1; i < n; i++) {
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i]);
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
            cooldown[i] = max(cooldown[i-1], sell[i-1]);
        }
        
        // The maximum profit is stored in the sell array
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
- The dynamic programming approach is useful for solving problems that have overlapping subproblems.
- The use of variables like buy, sell, and cooldown helps to break down the problem into manageable subproblems.
- The time complexity of the solution is O(n), where n is the number of days, because we only need to iterate through the prices array once.