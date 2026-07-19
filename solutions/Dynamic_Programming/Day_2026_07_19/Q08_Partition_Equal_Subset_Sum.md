# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. Each element in the array can only be used once. The array contains only positive integers and the sum of the array elements will not exceed 200.

## Approach
The problem can be solved using dynamic programming by calculating the total sum of the array and checking if it's possible to get a subset with a sum equal to half of the total sum. The idea is to build a DP table where each cell represents whether a sum is achievable or not.

## Complexity
- Time: O(n*sum)
- Space: O(n*sum)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for (int num : nums) sum += num;
        
        // If the sum is odd, it's impossible to partition the array into two subsets with equal sum
        if (sum % 2 != 0) return false;
        
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
Input: nums = [1,5,11,5]
Output: true
Input: nums = [1,2,3,5]
Output: false
```

## Key Takeaways
- The problem can be solved using dynamic programming by calculating the total sum of the array and checking if it's possible to get a subset with a sum equal to half of the total sum.
- The time complexity is O(n*sum) where n is the number of elements in the array and sum is the total sum of the array elements.
- The space complexity is O(n*sum) which is used to store the DP table.