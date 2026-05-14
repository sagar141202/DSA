# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The problem requires finding the total count of combinations that sum up to the target, where the order of the numbers in the combination does matter.

## Approach
The problem can be solved using dynamic programming by building up a table where each cell represents the number of combinations that sum up to a certain value. The algorithm iterates through the numbers from 1 to the target and for each number, it calculates the number of combinations by considering all possible previous numbers.

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
        
        // Iterate through all possible sums from 1 to target
        for (int i = 1; i <= target; i++) {
            // For each sum, iterate through all numbers in nums
            for (int num : nums) {
                // If the current number is less than or equal to the current sum
                if (num <= i) {
                    // Add the number of combinations for the sum minus the current number
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
Input: nums = [1, 2, 3], target = 4
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
- Use dynamic programming to build up a table of combinations for each sum.
- Iterate through all possible sums and numbers to calculate the combinations.
- The order of the numbers in the combination matters, so we need to consider all possible previous numbers when calculating the combinations.