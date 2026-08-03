# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The solution should be able to handle large inputs and should be efficient.

## Approach
We can solve this problem using Dynamic Programming, where we build up a table of combinations for each number up to the target. The key insight is that the number of combinations for a given number is the sum of the combinations for the numbers that are less than or equal to it. We use a bottom-up approach to fill up the table.

## Complexity
- Time: O(target * n)
- Space: O(target)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        // Create a DP table to store the combinations for each number up to the target
        vector<int> dp(target + 1, 0);
        
        // Base case: there is one way to make 0 (by not choosing any numbers)
        dp[0] = 1;
        
        // Fill up the table using a bottom-up approach
        for (int i = 1; i <= target; i++) {
            // For each number, try to use each number in nums to make it
            for (int num : nums) {
                // If the current number is less than or equal to the target, add the combinations for the remaining amount
                if (i - num >= 0) {
                    dp[i] += dp[i - num];
                }
            }
        }
        
        // The answer is the number of combinations for the target
        return dp[target];
    }
};
```

## Test Cases
```
Input: nums = [1, 2, 3], target = 4
Output: 7
Explanation: The combinations are:
1 + 1 + 1 + 1
1 + 1 + 2
1 + 2 + 1
1 + 3
2 + 1 + 1
2 + 2
3 + 1
```

## Key Takeaways
- Use Dynamic Programming to build up a table of combinations for each number up to the target.
- The key insight is that the number of combinations for a given number is the sum of the combinations for the numbers that are less than or equal to it.
- The solution has a time complexity of O(target * n) and a space complexity of O(target), making it efficient for large inputs.