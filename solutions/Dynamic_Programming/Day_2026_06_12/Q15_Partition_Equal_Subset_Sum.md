# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. The length of the array is in the range `[1, 200]`. The total sum of elements in the array is in the range `[1, 10^4]`. For example, given `nums = [1, 5, 11, 5]`, the output should be `true` because the array can be partitioned into `[1, 5, 5]` and `[11]`, both having a sum of `11`. However, given `nums = [1, 2, 3, 9]`, the output should be `false` because there is no way to partition the array into two subsets with equal sums.

## Approach
This problem can be solved using dynamic programming by calculating the possible sums that can be achieved using the given numbers. The idea is to find if the total sum of the array can be divided into two equal parts. We can use a boolean array `dp` where `dp[i]` is `true` if a sum of `i` can be achieved.

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

int main() {
    Solution solution;
    vector<int> nums = {1, 5, 11, 5};
    cout << boolalpha << solution.canPartition(nums) << endl;
    return 0;
}
```

## Test Cases
```
Input: nums = [1, 5, 11, 5]
Output: true
Input: nums = [1, 2, 3, 9]
Output: false
```

## Key Takeaways
- The problem can be reduced to finding if a subset with a sum equal to half of the total sum exists.
- Dynamic programming can be used to efficiently calculate all possible sums.
- The space complexity can be optimized by using a 1D array instead of a 2D array.