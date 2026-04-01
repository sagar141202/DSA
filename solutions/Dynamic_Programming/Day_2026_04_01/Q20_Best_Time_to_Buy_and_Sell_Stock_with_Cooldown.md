# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
You are given an array of integers representing the prices of a stock over time. You can buy and sell the stock, but you must wait at least one day after selling before you can buy again. The goal is to find the maximum profit that can be achieved. The prices array will have at least one element, and all elements will be non-negative integers. For example, if the input is [1, 2, 3, 0, 2], the output should be 3, which is achieved by buying at price 1, selling at price 3, and then buying at price 0 and selling at price 2.

## Approach
The problem can be solved using dynamic programming by maintaining three arrays: buy, sell, and cooldown. The buy array stores the maximum profit after buying the stock, the sell array stores the maximum profit after selling the stock, and the cooldown array stores the maximum profit after a cooldown period.

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
- The dynamic programming approach allows us to break down the problem into smaller subproblems and solve them efficiently.
- The use of three arrays (buy, sell, and cooldown) helps to keep track of the maximum profit at each step.
- The time complexity of O(n) makes the solution efficient for large inputs.