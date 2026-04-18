# Best Time to Buy and Sell Stock

## Problem Statement
Given an array of integers representing the daily stock prices, find the maximum possible profit that can be achieved by buying and selling the stock at most twice. The stock can only be sold after it is bought, and the same stock cannot be bought and sold on the same day. The input array will contain at least one element, and all elements will be non-negative integers. For example, if the input array is [3, 3, 5, 0, 0, 3, 1, 4], the maximum possible profit is 6, which can be achieved by buying on day 0, selling on day 2, buying on day 4, and selling on day 7.

## Approach
The problem can be solved using dynamic programming, where we maintain arrays to store the maximum profit after the first buy, first sell, second buy, and second sell. We iterate through the array, updating these values based on the current price. The maximum possible profit will be the value stored in the second sell array at the end of the iteration.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // base case
        if (prices.size() < 2) {
            return 0;
        }

        int n = prices.size();
        vector<int> firstBuy(n, 0), firstSell(n, 0), secondBuy(n, 0), secondSell(n, 0);

        // initialize first buy and second buy as the negative of the first price
        firstBuy[0] = -prices[0];
        secondBuy[0] = -prices[0];

        // fill up the arrays using dynamic programming
        for (int i = 1; i < n; i++) {
            firstBuy[i] = max(firstBuy[i - 1], -prices[i]);
            firstSell[i] = max(firstSell[i - 1], firstBuy[i - 1] + prices[i]);
            secondBuy[i] = max(secondBuy[i - 1], firstSell[i - 1] - prices[i]);
            secondSell[i] = max(secondSell[i - 1], secondBuy[i - 1] + prices[i]);
        }

        // the maximum possible profit is stored in the second sell array at the end
        return secondSell[n - 1];
    }
};
```

## Test Cases
```
Input: [3, 3, 5, 0, 0, 3, 1, 4]
Output: 6
Input: [1, 2, 3, 4, 5]
Output: 4
Input: [7, 6, 4, 3, 1]
Output: 0
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems.
- Maintain separate arrays to store the maximum profit after each buy and sell.
- Update the arrays iteratively based on the current price.