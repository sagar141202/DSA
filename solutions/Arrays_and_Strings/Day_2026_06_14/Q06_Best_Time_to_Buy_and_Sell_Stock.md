# Best Time to Buy and Sell Stock

## Problem Statement
You are given an array of integers representing the daily stock prices. The task is to find the maximum possible profit that can be achieved by buying and selling the stock once. You must buy the stock before selling it, and you cannot sell the stock before buying it. The stock prices are given for each day, and you can only buy and sell the stock on a day when the market is open. For example, if the input array is [7, 1, 5, 3, 6, 4], the maximum possible profit is 5, which can be achieved by buying the stock on the second day (price = 1) and selling it on the fifth day (price = 6).

## Approach
The algorithm uses a simple iterative approach to find the maximum possible profit. It maintains two variables: the minimum price encountered so far and the maximum profit that can be achieved. The algorithm iterates through the array of stock prices, updating the minimum price and the maximum profit at each step.

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
            // Update the minimum price
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            }
            // Update the maximum profit
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
- The algorithm has a time complexity of O(n), where n is the number of days in the input array.
- The algorithm has a space complexity of O(1), which means it uses a constant amount of space.
- The algorithm iterates through the array of stock prices only once, making it efficient for large inputs.