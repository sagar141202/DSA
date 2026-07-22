# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. Each element in `nums` can only be used once in the partition. Return `true` if the array can be partitioned into two subsets with equal sum, otherwise return `false`. The length of `nums` is between 1 and 200, and the sum of `nums` is between 1 and 10000. For example, given `nums = [1, 5, 11, 5]`, the function should return `true` because `nums` can be partitioned into `[1, 5, 5]` and `[11]` with equal sum.

## Approach
The problem can be solved using dynamic programming by calculating the possible sums that can be achieved using the first `i` elements of the array. We can use a 2D table to store the intermediate results, where `dp[i][j]` represents whether the sum `j` can be achieved using the first `i` elements.

## Complexity
- Time: O(n*sum), where n is the number of elements in the array and sum is the total sum of the array.
- Space: O(n*sum), for the 2D table used to store the intermediate results.

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
        
        // If the sum is odd, it's impossible to partition the array into two subsets with equal sum.
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

Input: nums = [1, 2, 3, 5]
Output: false
```

## Key Takeaways
- The problem can be solved using dynamic programming by calculating the possible sums that can be achieved using the first `i` elements of the array.
- The time complexity of the solution is O(n*sum), where n is the number of elements in the array and sum is the total sum of the array.
- The space complexity of the solution is O(n*sum), for the 2D table used to store the intermediate results.