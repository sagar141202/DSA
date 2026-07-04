# Best Time to Buy and Sell Stock

## Problem Statement
Given an array of integers representing the daily stock prices, find the maximum possible profit that can be achieved by buying and selling the stock once. The stock can only be bought before it is sold, and the selling price must be higher than the buying price. For example, if the input array is [7, 1, 5, 3, 6, 4], the maximum possible profit is 5, which can be achieved by buying the stock at price 1 and selling it at price 6.

## Approach
The algorithm uses a single pass through the array to find the maximum profit. It maintains two variables: the minimum price encountered so far and the maximum profit that can be achieved. The maximum profit is updated whenever a higher profit is found.

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
        if (prices.size() < 2) {
            return 0;
        }
        
        int minPrice = prices[0];
        int maxProfit = 0;
        
        for (int i = 1; i < prices.size(); i++) {
            // Update minPrice if current price is lower
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            }
            // Update maxProfit if current profit is higher
            else if (prices[i] - minPrice > maxProfit) {
                maxProfit = prices[i] - minPrice;
            }
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
- The algorithm only needs a single pass through the array to find the maximum possible profit.
- The minimum price encountered so far is updated whenever a lower price is found.
- The maximum profit is updated whenever a higher profit is found by subtracting the minimum price from the current price.