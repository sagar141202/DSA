# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
You are given an array of integers representing the prices of a stock over time. The goal is to find the maximum profit that can be achieved by buying and selling the stock, with the constraint that you cannot buy a stock on the day after selling a stock (cooldown period). The input array `prices` is a list of non-negative integers, where `prices[i]` is the price of the stock on the `i-th` day.

## Approach
We will use dynamic programming to solve this problem, where we maintain three variables: `buy`, `sell`, and `cooldown`, representing the maximum profit when the last action was buying, selling, or cooling down, respectively. We iterate through the prices array and update these variables accordingly.

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
            int newBuy = max(buy, cooldown - price);
            int newSell = max(sell, buy + price);
            int newCooldown = max(cooldown, sell);
            buy = newBuy;
            sell = newSell;
            cooldown = newCooldown;
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
- We use a bottom-up dynamic programming approach to solve this problem, where we start from the first day and build up the solution.
- The `buy`, `sell`, and `cooldown` variables are updated at each step based on the maximum profit that can be achieved.
- The final result is stored in the `sell` variable, which represents the maximum profit that can be achieved after the cooldown period.