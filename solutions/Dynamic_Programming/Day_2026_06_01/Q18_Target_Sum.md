# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of ways to assign + or - sign to each integer in the array such that the sum of the resulting array equals the target sum. The array can contain both positive and negative integers, and the target sum can also be positive or negative. For example, given the array [1, 1, 1, 1, 1] and a target sum of 3, there are 5 ways to achieve this sum: [1, 1, 1, -1, 1], [1, 1, -1, 1, 1], [1, -1, 1, 1, 1], [-1, 1, 1, 1, 1], and [1, 1, 1, 1, -1].

## Approach
We will use dynamic programming to solve this problem by maintaining a DP array where each index represents a possible sum. We iterate over the array and for each element, we update the DP array by adding or subtracting the current element from the existing sums. The final answer will be the value at the index representing the target sum in the DP array.

## Complexity
- Time: O(n * sum), where n is the number of elements in the array and sum is the sum of all elements in the array.
- Space: O(sum), where sum is the sum of all elements in the array.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int sum = 0;
        for (int num : nums) sum += num;
        
        if (S > sum || S < -sum) return 0;
        
        int n = nums.size();
        vector<vector<int>> dp(n + 1, vector<int>(2 * sum + 1, 0));
        
        dp[0][sum] = 1;
        
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= 2 * sum; j++) {
                if (dp[i - 1][j] == 0) continue;
                if (j - nums[i - 1] >= 0) dp[i][j - nums[i - 1]] += dp[i - 1][j];
                if (j + nums[i - 1] <= 2 * sum) dp[i][j + nums[i - 1]] += dp[i - 1][j];
            }
        }
        
        return dp[n][sum + S];
    }
};
```

## Test Cases
```
Input: nums = [1, 1, 1, 1, 1], S = 3
Output: 5
Input: nums = [1], S = 1
Output: 1
```

## Key Takeaways
- The problem can be solved using dynamic programming by maintaining a DP array where each index represents a possible sum.
- The time complexity of the solution is O(n * sum), where n is the number of elements in the array and sum is the sum of all elements in the array.
- The space complexity of the solution is O(sum), where sum is the sum of all elements in the array.