# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The problem requires finding the total count of combinations, considering all possible combinations of numbers that sum up to the target.

## Approach
The problem can be solved using dynamic programming, where we build up a table to store the number of combinations for each possible sum from 1 to the target. We iterate over each number in the array and update the table accordingly. The final result will be stored in the table at the index corresponding to the target sum.

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
        
        // Iterate over each possible sum from 1 to the target
        for (int i = 1; i <= target; i++) {
            // For each number in the array, update the table if the current number is less than or equal to the current sum
            for (int num : nums) {
                if (num <= i) {
                    dp[i] += dp[i - num];
                }
            }
        }
        
        // The final result is stored in the table at the index corresponding to the target sum
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
- The problem can be solved using dynamic programming by building up a table to store the number of combinations for each possible sum.
- The time complexity is O(n*target) due to the nested loops, where n is the size of the input array.
- The space complexity is O(target) for storing the dp table.