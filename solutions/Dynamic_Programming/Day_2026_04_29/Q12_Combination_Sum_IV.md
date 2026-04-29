# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `nums` can be used any number of times in the combination. The problem can be solved using dynamic programming, where we build up a table of combinations for each number up to the target. For example, if `nums = [1, 2, 3]` and `target = 4`, the output should be `7` because there are seven combinations that sum up to `4`: `[1, 1, 1, 1]`, `[1, 1, 2]`, `[1, 2, 1]`, `[1, 3]`, `[2, 1, 1]`, `[2, 2]`, and `[3, 1]`.

## Approach
We use dynamic programming to solve this problem, where we create a table `dp` of size `target + 1` and initialize it with zeros. We then fill up the table by iterating over each number in `nums` and updating the table accordingly. The final result is stored in `dp[target]`.

## Complexity
- Time: O(n*target)
- Space: O(target)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        // Create a table to store the number of combinations for each number up to the target
        vector<int> dp(target + 1, 0);
        
        // Base case: there is one way to make 0, which is to not include any numbers
        dp[0] = 1;
        
        // Fill up the table
        for (int i = 1; i <= target; i++) {
            // For each number in nums, update the table if it is less than or equal to the current number
            for (int num : nums) {
                if (i - num >= 0) {
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
- We use dynamic programming to solve this problem, which allows us to avoid redundant calculations and improve efficiency.
- The time complexity is O(n*target), where n is the size of the input array `nums`, because we need to iterate over each number in `nums` for each number up to the target.
- The space complexity is O(target), because we need to store the table `dp` of size `target + 1`.