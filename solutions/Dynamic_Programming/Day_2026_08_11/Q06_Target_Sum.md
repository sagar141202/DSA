# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets that sum up to the target sum. The array can contain both positive and negative integers. The problem can be formally defined as: given an integer array `nums` and an integer `target`, return the number of subsets that sum up to `target`. The constraints are: `1 <= nums.length <= 20`, `-10^6 <= nums[i] <= 10^6`, and `-10^6 <= target <= 10^6`.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array `dp` where `dp[i][j]` represents the number of subsets of the array from index `0` to `i` that sum up to `j`. The final answer will be stored in `dp[n][target]`, where `n` is the size of the array.

## Complexity
- Time: O(n * sum), where n is the size of the array and sum is the sum of all elements in the array
- Space: O(n * sum)

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
        
        // If the target is greater than the sum of all elements, it's impossible to reach the target
        if (abs(target) > sum) return 0;
        
        // Create a 2D array to store the number of subsets that sum up to each possible sum
        int dp[n][2 * sum + 1] = {};
        
        // Base case: there is one way to reach a sum of 0 with an empty subset
        dp[0][sum] = 1;
        
        // Fill up the dp array
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 2 * sum + 1; j++) {
                if (dp[i][j] == 0) continue;
                
                // Add the current number to the subset
                if (j + nums[i] < 2 * sum + 1) {
                    dp[i + 1][j + nums[i]] += dp[i][j];
                }
                
                // Subtract the current number from the subset
                if (j - nums[i] >= 0) {
                    dp[i + 1][j - nums[i]] += dp[i][j];
                }
            }
        }
        
        // The final answer is stored in dp[n][sum + target]
        return dp[n][sum + target];
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
- The problem can be solved using dynamic programming by maintaining a 2D array to store the number of subsets that sum up to each possible sum.
- The time complexity is O(n * sum), where n is the size of the array and sum is the sum of all elements in the array.
- The space complexity is O(n * sum), which can be optimized by using a 1D array instead of a 2D array.