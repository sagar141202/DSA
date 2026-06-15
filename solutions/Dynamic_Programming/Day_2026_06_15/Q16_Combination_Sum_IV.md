# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The problem statement requires us to find the total count of combinations that can form the target sum. For example, if `nums = [1, 2, 3]` and `target = 4`, the output should be `7` because there are `7` combinations that sum up to `4`: `[1, 1, 1, 1]`, `[1, 1, 2]`, `[1, 2, 1]`, `[1, 3]`, `[2, 1, 1]`, `[2, 2]`, and `[3, 1]`.

## Approach
The problem can be solved using dynamic programming by building up a table where each cell represents the number of combinations that sum up to a certain value. We start from the base case where the sum is `0` and then fill up the table iteratively. The algorithm uses the concept of combinatorics and dynamic programming to efficiently calculate the total count of combinations.

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
        // Create a dp table to store the number of combinations for each sum
        vector<int> dp(target + 1, 0);
        
        // Base case: there is one way to get a sum of 0 (by not picking any numbers)
        dp[0] = 1;
        
        // Fill up the dp table iteratively
        for (int i = 1; i <= target; i++) {
            // For each number in nums, add the number of combinations that sum up to i - num
            for (int num : nums) {
                if (i - num >= 0) {
                    dp[i] += dp[i - num];
                }
            }
        }
        
        // Return the total count of combinations that sum up to target
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
- Use dynamic programming to build up a table where each cell represents the number of combinations that sum up to a certain value.
- The algorithm has a time complexity of O(n*target) and a space complexity of O(target), where n is the size of the input array `nums`.
- The solution uses the concept of combinatorics and dynamic programming to efficiently calculate the total count of combinations.