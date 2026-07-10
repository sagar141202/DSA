# Best Time to Buy and Sell Stock

## Problem Statement
Given an array of integers representing the daily stock prices, find the maximum possible profit that can be achieved by buying and selling the stock once. The stock can only be sold after it is bought, and the profit is calculated as the difference between the selling price and the buying price. For example, if the input array is [7, 1, 5, 3, 6, 4], the maximum possible profit is 5, which can be achieved by buying the stock on the second day (price = 1) and selling it on the fifth day (price = 6).

## Approach
The algorithm uses a simple one-pass approach, iterating through the array to find the minimum price and the maximum profit that can be achieved. It keeps track of the minimum price encountered so far and the maximum profit that can be achieved by selling at the current price.

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
        if (prices.empty()) {
            return 0;
        }
        
        int minPrice = prices[0];
        int maxProfit = 0;
        
        for (int i = 1; i < prices.size(); i++) {
            // update minPrice if current price is smaller
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            }
            // update maxProfit if current profit is larger
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
- The algorithm only needs to iterate through the array once, making it efficient for large inputs.
- The use of two variables, `minPrice` and `maxProfit`, allows the algorithm to keep track of the minimum price and the maximum profit that can be achieved in a single pass.