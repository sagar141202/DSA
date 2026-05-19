# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets that sum up to the target sum. The array can contain both positive and negative integers, and each element can be used only once. The target sum can be any integer, positive, negative, or zero. For example, given the array [1, 1, 1, 1, 1] and a target sum of 3, the subsets that sum up to 3 are [1, 1, 1] and [1, 1, 1], so the output should be 5.

## Approach
The problem can be solved using dynamic programming by building a 2D table where each cell represents the number of subsets that sum up to a certain value. The algorithm iterates over the array and updates the table based on whether the current element is included in the subset or not. The final result is stored in the cell corresponding to the target sum.

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
        for (int j = 0; j <= 2 * sum; j++) {
            if (j - nums[i - 1] >= 0 && j - nums[i - 1] <= 2 * sum) {
                dp[i][j] += dp[i - 1][j - nums[i - 1]];
            }
            if (j + nums[i - 1] >= 0 && j + nums[i - 1] <= 2 * sum) {
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
```

## Key Takeaways
- The problem can be solved using dynamic programming with a time complexity of O(n*sum) and a space complexity of O(n*sum).
- The 2D table is used to store the number of subsets that sum up to a certain value, and the final result is stored in the cell corresponding to the target sum.
- The algorithm iterates over the array and updates the table based on whether the current element is included in the subset or not.