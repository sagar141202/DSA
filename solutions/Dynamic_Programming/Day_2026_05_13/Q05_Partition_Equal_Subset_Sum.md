# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. The length of the input array is in the range [1, 200] and the sum of all elements in the input array is in the range [1, 10^4]. The array can contain duplicate elements and the elements are not necessarily distinct.

## Approach
We will use dynamic programming to solve this problem, calculating the possible sums that can be obtained from the array elements. The approach involves iterating over the array and updating a boolean array `dp` where `dp[i]` is `true` if the sum `i` can be obtained from the array elements.

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
        
        // If the sum is odd, it's impossible to partition the array into two subsets with equal sum
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
- The problem can be solved using dynamic programming by iterating over the array and updating a boolean array `dp` where `dp[i]` is `true` if the sum `i` can be obtained from the array elements.
- The time complexity of the solution is O(n * sum) where n is the length of the input array and sum is the sum of all elements in the input array.
- The space complexity of the solution is O(sum) for the boolean array `dp`.