# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. Each element in the array can only be used once in the partition. The array cannot be modified, and the solution must be achieved using dynamic programming. The function should return `true` if the array can be partitioned into two subsets with equal sum, and `false` otherwise. The constraints are: `1 <= nums.length <= 200`, `1 <= nums[i] <= 100`.

## Approach
The algorithm uses dynamic programming to calculate all possible subset sums. It iterates over each number in the array and updates the possible subset sums. The base case is when the target sum is 0, which is always achievable. The function returns true if the target sum (half of the total sum) is achievable.

## Complexity
- Time: O(n * sum), where n is the number of elements and sum is the total sum of the array
- Space: O(sum), where sum is the total sum of the array

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        if (sum % 2 != 0) {
            return false;
        }
        int target = sum / 2;
        vector<bool> dp(target + 1, false);
        dp[0] = true;
        for (int num : nums) {
            for (int i = target; i >= num; i--) {
                if (dp[i - num]) {
                    dp[i] = true;
                }
            }
        }
        return dp[target];
    }
};
```

## Test Cases
```
Input: nums = [1,5,11,5]
Output: true
Input: nums = [1,2,3,5]
Output: false
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems.
- The `canPartition` function returns `true` if the array can be partitioned into two subsets with equal sum.
- The time complexity of the solution is O(n * sum), where n is the number of elements and sum is the total sum of the array.