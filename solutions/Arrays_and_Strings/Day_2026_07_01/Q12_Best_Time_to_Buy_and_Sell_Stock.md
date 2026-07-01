# Best Time to Buy and Sell Stock

## Problem Statement
You are given an array of integers representing the daily stock prices. The task is to find the best time to buy and sell a stock to maximize the profit. The constraint is that you can only buy and sell the stock once, and you cannot sell the stock before buying it. For example, if the input array is [7, 1, 5, 3, 6, 4], the output should be 5, which is the maximum possible profit.

## Approach
The algorithm uses a dynamic programming approach to keep track of the minimum price encountered so far and the maximum profit that can be achieved. It iterates through the array, updating the minimum price and maximum profit at each step. The maximum profit is calculated by subtracting the minimum price from the current price.

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
        // initialize minimum price and maximum profit
        int minPrice = INT_MAX;
        int maxProfit = 0;
        
        // iterate through the array
        for (int price : prices) {
            // update minimum price
            minPrice = min(minPrice, price);
            // update maximum profit
            maxProfit = max(maxProfit, price - minPrice);
        }
        
        return maxProfit;
    }
};
```

## Test Cases
```
Input: [7, 1, 5, 3, 6, 4]
Output: 5
Input: [7, 6, 4, 3, 1]
Output: 0
```

## Key Takeaways
- The algorithm has a time complexity of O(n), where n is the number of days.
- The algorithm has a space complexity of O(1), as it only uses a constant amount of space to store the minimum price and maximum profit.
- The algorithm can be applied to any array of integers representing daily stock prices.