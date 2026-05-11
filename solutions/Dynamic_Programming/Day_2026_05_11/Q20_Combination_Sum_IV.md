# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The solution should be able to handle a large input size.

## Approach
The problem can be solved using dynamic programming, where we build up a table of combinations for each sum from 1 to the target. We iterate over each number in the array and update the table accordingly. This approach ensures that we consider all possible combinations.

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
        
        // Base case: there is one way to get a sum of 0 (by not using any numbers)
        dp[0] = 1;
        
        // Iterate over each possible sum
        for (int i = 1; i <= target; i++) {
            // Iterate over each number in the array
            for (int num : nums) {
                // If the current number is less than or equal to the current sum
                if (num <= i) {
                    // Update the dp table with the number of combinations for the current sum
                    dp[i] += dp[i - num];
                }
            }
        }
        
        // Return the number of combinations for the target sum
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
- The dynamic programming approach allows us to efficiently compute the number of combinations for each sum.
- The time complexity is O(n*target) because we iterate over each number in the array for each possible sum.
- The space complexity is O(target) because we need to store the dp table for each possible sum.