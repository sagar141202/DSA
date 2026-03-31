# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets that sum up to the target sum. The array can contain both positive and negative integers. The problem can be solved using dynamic programming.

## Approach
The algorithm uses a dynamic programming approach to build up a table of subset sums. It iterates over the array and for each element, it updates the table with the new subset sums. The final result is the number of subsets that sum up to the target sum.

## Complexity
- Time: O(n*sum)
- Space: O(n*sum)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findTargetSumWays(vector<int>& nums, int target) {
    int sum = 0;
    for (int num : nums) {
        sum += num;
    }
    if (target > sum || target < -sum) {
        return 0;
    }
    int offset = sum;
    vector<vector<int>> dp(nums.size() + 1, vector<int>(2 * sum + 1, 0));
    dp[0][offset] = 1;
    for (int i = 1; i <= nums.size(); i++) {
        for (int j = 0; j < 2 * sum + 1; j++) {
            if (j - nums[i - 1] >= 0 && j - nums[i - 1] < 2 * sum + 1) {
                dp[i][j] += dp[i - 1][j - nums[i - 1]];
            }
            if (j + nums[i - 1] >= 0 && j + nums[i - 1] < 2 * sum + 1) {
                dp[i][j] += dp[i - 1][j + nums[i - 1]];
            }
        }
    }
    return dp[nums.size()][offset + target];
}

int main() {
    vector<int> nums = {1, 1, 1, 1, 1};
    int target = 3;
    cout << findTargetSumWays(nums, target) << endl;
    return 0;
}
```

## Test Cases
```
Input: nums = [1, 1, 1, 1, 1], target = 3
Output: 5
Input: nums = [1], target = 1
Output: 1
```

## Key Takeaways
- The problem can be solved using dynamic programming with a time complexity of O(n*sum) and a space complexity of O(n*sum).
- The dynamic programming table is used to store the number of subsets that sum up to each possible sum.
- The final result is the number of subsets that sum up to the target sum.