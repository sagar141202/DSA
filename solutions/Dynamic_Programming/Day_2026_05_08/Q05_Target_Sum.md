# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets that sum up to the target sum. The array can contain both positive and negative integers. The problem can be formally defined as: given an array `nums` of size `n` and a target sum `S`, find the number of subsets of `nums` that sum up to `S`. For example, if `nums = [1, 1, 1, 1, 1]` and `S = 3`, the subsets that sum up to `S` are `[1, 1, 1]`, `[1, 1, 1]`, `[1, 1, 1]`, `[1, 1, 1]`, and `[1, 1, 1]`, so the answer is `5`.

## Approach
The problem can be solved using dynamic programming by building a 2D table where each cell `dp[i][j]` represents the number of subsets of the first `i` elements that sum up to `j`. The final answer will be stored in `dp[n][S]`. We can fill up the table by iterating over the array and for each element, we have two choices: include it in the subset or not.

## Complexity
- Time: O(n*S)
- Space: O(n*S)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findTargetSumWays(vector<int>& nums, int S) {
    int n = nums.size();
    int sum = 0;
    for (int num : nums) sum += num;
    if (S > sum || S < -sum) return 0;
    int offset = sum;
    vector<vector<int>> dp(n + 1, vector<int>(2 * sum + 1, 0));
    dp[0][offset] = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= 2 * sum; j++) {
            if (j - nums[i - 1] >= 0) dp[i][j] += dp[i - 1][j - nums[i - 1]];
            if (j + nums[i - 1] <= 2 * sum) dp[i][j] += dp[i - 1][j + nums[i - 1]];
        }
    }
    return dp[n][S + offset];
}

int main() {
    vector<int> nums = {1, 1, 1, 1, 1};
    int S = 3;
    cout << findTargetSumWays(nums, S) << endl;
    return 0;
}
```

## Test Cases
```
Input: nums = [1, 1, 1, 1, 1], S = 3
Output: 5
```

## Key Takeaways
- The problem can be solved using dynamic programming by building a 2D table where each cell represents the number of subsets that sum up to a certain value.
- The time complexity is O(n*S) where n is the size of the array and S is the target sum.
- The space complexity is O(n*S) for storing the 2D table.