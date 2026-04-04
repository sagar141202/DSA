# Target Sum

## Problem Statement
Given an array of integers, find the number of ways to assign a plus or minus sign to each integer such that the sum of the resulting array equals a given target. The array can contain both positive and negative integers, and the target can also be positive or negative. The function should return the number of ways to achieve the target sum.

## Approach
The problem can be solved using dynamic programming by maintaining a count of the number of ways to reach each possible sum. The algorithm iterates through the array, updating the count of ways to reach each sum by considering both the plus and minus sign for each integer.

## Complexity
- Time: O(n * sum), where n is the size of the array and sum is the maximum possible sum
- Space: O(sum), where sum is the maximum possible sum

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int n = nums.size();
        int sum = 0;
        for (int num : nums) sum += num;
        
        // If the target is greater than the sum of all numbers or less than the negative sum of all numbers, return 0
        if (abs(target) > sum) return 0;
        
        // Initialize a 2D array to store the number of ways to reach each sum
        vector<vector<int>> dp(n, vector<int>(2 * sum + 1, 0));
        
        // Base case: there is one way to reach a sum of 0 (by not including any numbers)
        dp[0][sum] = 1;
        
        // Iterate through the array
        for (int i = 1; i < n; i++) {
            // Iterate through each possible sum
            for (int j = 0; j < 2 * sum + 1; j++) {
                // If the current sum is not reachable, skip it
                if (dp[i - 1][j] == 0) continue;
                
                // Update the count of ways to reach the current sum plus the current number
                if (j - nums[i] >= 0) dp[i][j - nums[i]] += dp[i - 1][j];
                // Update the count of ways to reach the current sum minus the current number
                if (j + nums[i] < 2 * sum + 1) dp[i][j + nums[i]] += dp[i - 1][j];
            }
        }
        
        // Return the number of ways to reach the target sum
        return dp[n - 1][sum + target];
    }
};
```

## Test Cases
```
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Input: nums = [1], target = 1
Output: 1
```

## Key Takeaways
- The problem can be solved using dynamic programming by maintaining a count of the number of ways to reach each possible sum.
- The algorithm iterates through the array, updating the count of ways to reach each sum by considering both the plus and minus sign for each integer.
- The time complexity is O(n * sum), where n is the size of the array and sum is the maximum possible sum.