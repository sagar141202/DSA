# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The problem is also known as "Combination Sum IV" on LeetCode. The constraints are: `1 <= nums.length <= 200`, `1 <= nums[i] <= 1000`, `1 <= target <= 1000`, and all elements in `nums` are distinct.

## Approach
We will use dynamic programming to solve this problem. The idea is to build up a table where each entry represents the number of combinations that sum up to a certain value. We start with a base case and iteratively fill up the table.

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
        
        // Base case: there is one way to get a sum of 0 (by not choosing any numbers)
        dp[0] = 1;
        
        // Fill up the dp table
        for (int i = 1; i <= target; i++) {
            // For each possible sum, try to reach it by using each number in nums
            for (int num : nums) {
                // If the current number is less than or equal to the current sum
                if (num <= i) {
                    // Add the number of combinations that sum up to i - num to the current sum
                    dp[i] += dp[i - num];
                }
            }
        }
        
        // The answer is the number of combinations that sum up to the target
        return dp[target];
    }
};
```

## Test Cases
```
Input: nums = [1,2,3], target = 4
Output: 7
Explanation: The possible combinations are:
1 + 1 + 1 + 1
1 + 1 + 2
1 + 2 + 1
1 + 3
2 + 1 + 1
2 + 2
3 + 1
```

## Key Takeaways
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The key to solving this problem is to recognize that each number in `nums` can be used any number of times in the combination.
- The time complexity is O(n*target) because we need to fill up a table of size `target` and for each entry, we need to iterate over all numbers in `nums`.