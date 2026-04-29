# Best Time to Buy and Sell Stock

## Problem Statement
You are given an array of integers representing the daily stock prices. The task is to find the maximum possible profit that can be achieved by buying and selling the stock once. The constraint is that you must buy the stock before selling it. For example, if the input array is [7, 1, 5, 3, 6, 4], the maximum possible profit is 5, which can be achieved by buying the stock at price 1 and selling it at price 6.

## Approach
The algorithm uses a simple iterative approach, keeping track of the minimum price seen so far and the maximum profit that can be achieved. It iterates over the array, updating the minimum price and maximum profit at each step. This approach ensures that we consider all possible buy and sell combinations.

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
        
        // Iterate over the array
        for (int price : prices) {
            // Update minimum price
            if (price < minPrice) {
                minPrice = price;
            }
            // Update maximum profit
            else if (price - minPrice > maxProfit) {
                maxProfit = price - minPrice;
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
- We only need to keep track of the minimum price seen so far to find the maximum possible profit.
- The algorithm has a linear time complexity, making it efficient for large inputs.
- The space complexity is constant, as we only use a fixed amount of space to store the minimum price and maximum profit.