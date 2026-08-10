# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
Given an array of integers representing the prices of a stock over time, find the maximum profit that can be achieved by buying and selling the stock with a cooldown period of one day after selling. The cooldown period means that after selling the stock, you cannot buy it again for one day. The problem has the following constraints: the input array will have at least one element, and all elements will be non-negative integers.

## Approach
The problem can be solved using dynamic programming by maintaining three variables: buy, sell, and cooldown. The buy variable stores the maximum profit when the last action is buying, the sell variable stores the maximum profit when the last action is selling, and the cooldown variable stores the maximum profit when the last action is cooldown.

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
        
        vector<int> buy(n, 0), sell(n, 0), cooldown(n, 0);
        buy[0] = -prices[0];
        
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
- The problem requires maintaining a state machine with three states: buy, sell, and cooldown.
- The maximum profit is calculated by considering the maximum profit of the previous state and the current action.
- Dynamic programming is used to store the maximum profit at each step and avoid redundant calculations.