# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The problem can be solved using dynamic programming, where we build up a solution by considering each number in `nums` and its contribution to the total sum. The constraints are: `1 <= nums.length <= 200`, `1 <= nums[i] <= 1000`, and `1 <= target <= 1000`. For example, if `nums = [1, 2, 3]` and `target = 4`, the output should be `7` because there are 7 combinations that sum up to `4`: `[1, 1, 1, 1]`, `[1, 1, 2]`, `[1, 2, 1]`, `[1, 3]`, `[2, 1, 1]`, `[2, 2]`, and `[3, 1]`.

## Approach
The algorithm uses dynamic programming to build up a solution by considering each number in `nums` and its contribution to the total sum. We create a DP array `dp` where `dp[i]` represents the number of combinations that sum up to `i`. We iterate over each number in `nums` and update the `dp` array accordingly. The final result is stored in `dp[target]`.

## Complexity
- Time: O(n*target)
- Space: O(target)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        // Create a DP array to store the number of combinations that sum up to i
        vector<int> dp(target + 1, 0);
        
        // Base case: there is one way to sum up to 0 (i.e., not using any numbers)
        dp[0] = 1;
        
        // Iterate over each number from 1 to target
        for (int i = 1; i <= target; i++) {
            // Iterate over each number in nums
            for (int num : nums) {
                // If the current number is less than or equal to i, we can use it in the combination
                if (num <= i) {
                    // Update the DP array: the number of combinations that sum up to i is the sum of the number of combinations that sum up to i - num and the number of combinations that sum up to i without using num
                    dp[i] += dp[i - num];
                }
            }
        }
        
        // The final result is stored in dp[target]
        return dp[target];
    }
};
```

## Test Cases
```
Input: nums = [1, 2, 3], target = 4
Output: 7
Input: nums = [9], target = 3
Output: 0
```

## Key Takeaways
- The problem can be solved using dynamic programming by considering each number in `nums` and its contribution to the total sum.
- The DP array `dp` is used to store the number of combinations that sum up to `i`, and the final result is stored in `dp[target]`.
- The time complexity is O(n*target) and the space complexity is O(target), where n is the length of `nums` and target is the target sum.