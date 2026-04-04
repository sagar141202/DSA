# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used an unlimited number of times in the combination. The problem can be solved using dynamic programming, where we build up a solution by breaking down the problem into smaller sub-problems. For example, if `nums = [1, 2, 3]` and `target = 4`, the output should be `7` because there are `7` combinations that sum up to `4`: `[1, 1, 1, 1]`, `[1, 1, 2]`, `[1, 2, 1]`, `[1, 3]`, `[2, 1, 1]`, `[2, 2]`, and `[3, 1]`.

## Approach
We can solve this problem using dynamic programming by initializing a DP array where `dp[i]` represents the number of combinations that sum up to `i`. We then iterate over the `nums` array and update the DP array accordingly. The algorithm has a time complexity of O(n*target) and a space complexity of O(target), where n is the size of the `nums` array.

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
        // Initialize a DP array with size target + 1
        vector<unsigned int> dp(target + 1, 0);
        
        // Base case: there is one way to sum up to 0 (i.e., not picking any number)
        dp[0] = 1;
        
        // Iterate over the DP array
        for (int i = 1; i <= target; i++) {
            // For each number in the nums array
            for (int num : nums) {
                // If the current number is less than or equal to the current target
                if (num <= i) {
                    // Update the DP array
                    dp[i] += dp[i - num];
                }
            }
        }
        
        // Return the number of combinations that sum up to the target
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
- Dynamic programming can be used to solve problems that have overlapping sub-problems.
- The DP array should be initialized carefully to handle the base case.
- The time complexity of the algorithm is O(n*target) and the space complexity is O(target), where n is the size of the `nums` array.