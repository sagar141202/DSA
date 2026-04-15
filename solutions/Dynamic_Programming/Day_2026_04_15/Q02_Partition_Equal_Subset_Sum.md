# Partition Equal Subset Sum

## Problem Statement
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal. The length of the input array is in the range [1, 200] and the total sum of elements is in the range [1, 10^4]. The array may contain duplicate elements.

## Approach
The problem is solved using dynamic programming, where we calculate the possible sums that can be achieved using the given array elements. We initialize a dp array with size equal to the total sum plus one and then fill it up based on whether a sum can be achieved or not. The final answer is determined by checking if the total sum divided by two can be achieved.

## Complexity
- Time: O(n*sum), where n is the size of the input array and sum is the total sum of the array elements.
- Space: O(sum), where sum is the total sum of the array elements.

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
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Input: nums = [1, 2, 3, 5]
Output: false
Explanation: It's impossible to partition the array into two subsets with equal sum.
```

## Key Takeaways
- The problem requires finding a subset of the given array that sums up to half of the total sum of the array.
- Dynamic programming is used to solve the problem efficiently by storing the intermediate results.
- The time complexity of the solution is O(n*sum), where n is the size of the input array and sum is the total sum of the array elements.