# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. Each element in `nums` can only be used once, and all elements must be used. The array has a length of at most 200, and the sum of all elements in the array is at most 1000. For example, given `nums = [1, 5, 11, 5]`, the function should return `true` because the array can be partitioned into `[1, 5, 5]` and `[11]`, which have equal sums.

## Approach
The problem can be solved using dynamic programming by calculating the possible sums that can be achieved with the given numbers. We iterate over each number and update the possible sums. The algorithm checks if it's possible to achieve a sum equal to half of the total sum of the array.

## Complexity
- Time: O(n * sum), where n is the number of elements in the array and sum is the total sum of the array.
- Space: O(sum), for storing the possible sums.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for (int num : nums) sum += num;
        if (sum % 2 != 0) return false;
        int target = sum / 2;
        vector<bool> dp(target + 1, false);
        dp[0] = true;
        for (int num : nums) {
            for (int i = target; i >= num; i--) {
                if (dp[i - num]) dp[i] = true;
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
- The problem can be solved using dynamic programming with a time complexity of O(n * sum).
- The space complexity is O(sum), where sum is the total sum of the array.
- The solution checks if the total sum of the array is odd, in which case it returns false because it's impossible to partition the array into two subsets with equal sums.