# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
Given an array of integers representing the daily stock prices, find the maximum profit that can be achieved by buying and selling stocks with a cooldown period of one day after each sale. The cooldown period means that after selling a stock, you cannot buy another stock on the next day. The problem has the following constraints: the input array will have at least one element, and the prices are non-negative integers.

## Approach
The problem can be solved using dynamic programming by maintaining three variables: buy, sell, and cooldown. The buy variable stores the maximum profit after buying a stock, the sell variable stores the maximum profit after selling a stock, and the cooldown variable stores the maximum profit after a cooldown period. The algorithm iterates through the prices array, updating these variables at each step.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = INT_MIN, sell = 0, cooldown = 0;
        for (int price : prices) {
            int tempBuy = max(buy, cooldown - price);
            int tempSell = max(sell, buy + price);
            int tempCooldown = max(cooldown, sell);
            buy = tempBuy;
            sell = tempSell;
            cooldown = tempCooldown;
        }
        return sell;
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
- The dynamic programming approach helps to avoid redundant calculations and optimize the solution.
- The use of three variables (buy, sell, and cooldown) allows us to track the maximum profit at each step and make informed decisions about buying and selling stocks.
- The time complexity is O(n), where n is the number of days (i.e., the length of the prices array), and the space complexity is O(1), as we only use a constant amount of space to store the variables.