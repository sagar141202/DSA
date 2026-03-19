# Best Time to Buy and Sell Stock

## Problem Statement
Given an array of integers representing the daily stock prices, find the maximum possible profit that can be achieved by buying and selling the stock once. The stock can only be bought before it is sold, and the profit is the difference between the selling price and the buying price. The input array will have at least one element, and all elements will be non-negative integers.

## Approach
The algorithm uses a dynamic programming approach to keep track of the minimum price seen so far and the maximum profit that can be achieved. It iterates through the array, updating the minimum price and maximum profit at each step. The maximum profit is calculated by subtracting the minimum price from the current price.

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
        // Initialize minimum price and maximum profit
        int minPrice = INT_MAX;
        int maxProfit = 0;
        
        // Iterate through the array
        for (int i = 0; i < prices.size(); i++) {
            // Update minimum price
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            }
            // Update maximum profit
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
Input: [7,1,5,3,6,4]
Output: 5
Input: [7,6,4,3,1]
Output: 0
```

## Key Takeaways
- We only need to keep track of the minimum price seen so far to calculate the maximum profit.
- The algorithm has a linear time complexity because it only requires a single pass through the array.
- The space complexity is constant because we only use a fixed amount of space to store the minimum price and maximum profit.