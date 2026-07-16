# Combination Sum IV

## Problem Statement
Given an array of distinct integers `candidates` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `candidates` may be used an unlimited number of times in the combination. The solution should be able to handle large inputs and provide the result in a reasonable amount of time. For example, if `candidates = [1, 2, 3]` and `target = 4`, the output should be `7` because there are `7` combinations that sum up to `4`: `[1, 1, 1, 1]`, `[1, 1, 2]`, `[1, 2, 1]`, `[1, 3]`, `[2, 1, 1]`, `[2, 2]`, and `[3, 1]`.

## Approach
The problem can be solved using dynamic programming, where we build up a table of combinations for each sum from `1` to `target`. We iterate over each candidate and update the table accordingly. The final result will be stored in the last entry of the table.

## Complexity
- Time: O(target * n), where n is the number of candidates
- Space: O(target), where target is the target sum

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int combinationSum4(vector<int>& candidates, int target) {
        // Create a table to store the number of combinations for each sum
        vector<unsigned int> dp(target + 1, 0);
        
        // Base case: there is one way to get a sum of 0 (by not picking any numbers)
        dp[0] = 1;
        
        // Iterate over each possible sum
        for (int i = 1; i <= target; i++) {
            // Iterate over each candidate
            for (int candidate : candidates) {
                // If the current candidate is less than or equal to the current sum
                if (candidate <= i) {
                    // Add the number of combinations for the remaining sum to the current sum
                    dp[i] += dp[i - candidate];
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
Input: candidates = [1, 2, 3], target = 4
Output: 7
Input: candidates = [9], target = 3
Output: 0
```

## Key Takeaways
- The problem can be solved using dynamic programming with a time complexity of O(target * n) and a space complexity of O(target).
- The solution iterates over each possible sum and updates the table accordingly.
- The final result is stored in the last entry of the table.