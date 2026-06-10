# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. The length of the array will not exceed 200. Each element in the array will be between 1 and 100, and the sum of all elements will not exceed 1000. For example, given `nums = [1, 5, 11, 5]`, return `true` because the array can be partitioned as `[1, 5, 5]` and `[11]` with equal sum.

## Approach
The problem can be solved by using dynamic programming to calculate all possible subset sums. We calculate the total sum of the array and check if it's odd or even. If it's odd, we return false because it's impossible to partition the array into two subsets with equal sum. If it's even, we use a dynamic programming approach to check if we can achieve half of the total sum.

## Complexity
- Time: O(n * sum)
- Space: O(sum)

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
Input: nums = [1, 5, 11, 5]
Output: true
Input: nums = [1, 2, 3, 5]
Output: false
```

## Key Takeaways
- The problem requires calculating the total sum of the array and checking if it's odd or even.
- Dynamic programming is used to calculate all possible subset sums and check if we can achieve half of the total sum.
- The solution has a time complexity of O(n * sum) and a space complexity of O(sum).