# Combination Sum IV

## Problem Statement
Given an array of distinct integers `nums` and a target integer `target`, return the number of combinations that sum up to `target`. The length of the combination is not limited, and each number in `nums` can be used any number of times in the combination. For example, if `nums = [1, 2, 3]` and `target = 4`, the combinations are `[1, 1, 1, 1]`, `[1, 1, 2]`, `[1, 3]`, and `[2, 2]`, so the output is `4`. The input array `nums` will have a length between `1` and `200`, and the values of `nums` will be between `1` and `1000`. The `target` will be between `1` and `1000`.

## Approach
We will use dynamic programming to solve this problem, where `dp[i]` represents the number of combinations that sum up to `i`. We will iterate over each number in `nums` and update `dp[i]` accordingly. This approach ensures that we consider all possible combinations.

## Complexity
- Time: O(n*t)
- Space: O(t)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<unsigned int> dp(target + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= target; i++) {
            for (int num : nums) {
                if (i >= num) {
                    dp[i] += dp[i - num];
                }
            }
        }
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
- Use dynamic programming to solve problems that have overlapping subproblems.
- Initialize the base case `dp[0] = 1` to represent the combination that sums up to 0.
- Iterate over each number in `nums` and update `dp[i]` accordingly to consider all possible combinations.