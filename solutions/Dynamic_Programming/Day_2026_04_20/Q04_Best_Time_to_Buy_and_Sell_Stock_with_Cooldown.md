# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
Given an array of integers representing the daily stock prices, find the maximum profit that can be achieved by buying and selling the stock with a cooldown period of one day. The cooldown period means that after selling the stock, we cannot buy it again on the next day. The constraints are that we can only hold one stock at a time and we must sell the stock before buying it again. For example, if the input is [1, 2, 3, 0, 2], the output should be 3, which is achieved by buying on day 0, selling on day 2, and then buying on day 4 and selling on day 4.

## Approach
The algorithm uses dynamic programming to track the maximum profit at each day. We maintain three variables: buy, sell, and cooldown, which represent the maximum profit when we have the stock, when we have sold the stock, and when we are in the cooldown period, respectively.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() < 2) return 0;
        
        vector<int> buy(prices.size()), sell(prices.size()), cooldown(prices.size());
        buy[0] = -prices[0];
        sell[0] = 0;
        cooldown[0] = 0;
        
        for (int i = 1; i < prices.size(); i++) {
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i]);
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
            cooldown[i] = max(cooldown[i-1], sell[i-1]);
        }
        
        return max(sell.back(), cooldown.back());
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
- We use dynamic programming to solve this problem, which reduces the time complexity to O(n).
- We maintain three variables: buy, sell, and cooldown, to track the maximum profit at each day.
- The final result is the maximum of sell and cooldown at the last day.