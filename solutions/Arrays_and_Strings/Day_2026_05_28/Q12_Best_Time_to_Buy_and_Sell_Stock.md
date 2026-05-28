# Best Time to Buy and Sell Stock

## Problem Statement
The problem requires finding the best time to buy and sell a stock to maximize profit. Given an array of daily stock prices, we need to find the maximum possible profit that can be achieved by buying and selling the stock once. The constraint is that we can only buy the stock before selling it, and we cannot sell the stock before buying it. For example, if the input array is [7, 1, 5, 3, 6, 4], the maximum profit that can be achieved is 5 (buy at 1 and sell at 6).

## Approach
We will use a simple iterative approach to solve this problem. The idea is to keep track of the minimum price seen so far and the maximum profit that can be achieved. We will iterate through the array and update these variables accordingly.

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
- We need to keep track of the minimum price seen so far to calculate the maximum possible profit.
- We should update the maximum profit whenever we find a larger profit.
- The time complexity of this solution is O(n), where n is the number of days (i.e., the size of the input array).