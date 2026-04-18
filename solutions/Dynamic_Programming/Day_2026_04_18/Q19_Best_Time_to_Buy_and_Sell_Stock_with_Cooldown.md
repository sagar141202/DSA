# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
You are given an array of integers representing the prices of a stock over time. You can buy and sell the stock, but you must wait at least one day after selling before buying again. The goal is to find the maximum possible profit. The prices array will have at least one element, and all elements will be non-negative integers. For example, if the input is [1, 2, 3, 0, 2], the output should be 3, because you can buy at price 1, sell at price 3, and then buy at price 0 and sell at price 2.

## Approach
The problem can be solved using dynamic programming by maintaining three variables: buy, sell, and cooldown. The buy variable represents the maximum profit after buying the stock, the sell variable represents the maximum profit after selling the stock, and the cooldown variable represents the maximum profit after waiting for at least one day.

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
- The dynamic programming approach helps to avoid redundant calculations and improve the efficiency of the solution.
- The use of three variables (buy, sell, and cooldown) allows us to keep track of the maximum profit at each step and make informed decisions about when to buy and sell the stock.
- The time complexity of O(n) is achieved by only iterating through the prices array once, where n is the number of elements in the array.