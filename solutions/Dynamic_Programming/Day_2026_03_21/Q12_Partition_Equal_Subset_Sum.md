# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. Each element in the array can only be used once in the partition. The array cannot be modified, and all elements must be used exactly once. For example, given `nums = [1, 5, 11, 5]`, the output should be `true` because the array can be partitioned as `[1, 5, 5]` and `[11]`. However, given `nums = [1, 2, 3, 9]`, the output should be `false` because it is not possible to partition the array into two subsets with equal sum.

## Approach
We will use dynamic programming to solve this problem by calculating the total sum of the array and checking if it's possible to get a subset with a sum equal to half of the total sum. The algorithm iterates over all numbers and for each number, it checks if including it in the subset exceeds the target sum or not.

## Complexity
- Time: O(n * sum), where n is the number of elements in the array and sum is the total sum of the array elements.
- Space: O(sum), for the dynamic programming table.

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
                dp[i] = dp[i] || dp[i - num];
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
Input: nums = [1, 2, 3, 9]
Output: false
```

## Key Takeaways
- The problem can be solved using dynamic programming by checking all possible subsets of the array.
- If the total sum of the array is odd, it's impossible to partition it into two subsets with equal sum.
- The time complexity of the solution is exponential in the size of the input array but can be optimized using dynamic programming to O(n * sum).