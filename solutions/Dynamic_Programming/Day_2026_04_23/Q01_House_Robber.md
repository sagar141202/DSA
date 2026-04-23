# House Robber

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money in each house, return the maximum amount of money you can rob tonight without alerting the police. The input array `nums` will have a length of at least 1 and at most 200, and each element will be between 1 and 1000.

## Approach
The problem can be solved using dynamic programming by maintaining two arrays, one for the maximum amount of money that can be robbed up to each house and another for the maximum amount of money that can be robbed up to each house without robbing the previous house. The algorithm iterates through the array, at each step deciding whether to rob the current house or not based on the maximum amount that can be obtained.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }
        vector<int> dp1(nums.size() - 1);
        vector<int> dp2(nums.size());
        
        dp1[0] = nums[0];
        dp2[0] = nums[0];
        dp2[1] = max(nums[0], nums[1]);
        
        for (int i = 1; i < nums.size() - 1; i++) {
            dp1[i] = max(dp1[i-1], nums[i] + (i >= 2 ? dp1[i-2] : 0));
        }
        
        for (int i = 2; i < nums.size(); i++) {
            dp2[i] = max(dp2[i-1], nums[i] + (i >= 2 ? dp2[i-2] : 0));
        }
        
        return max(dp1[nums.size() - 2], dp2[nums.size() - 1]);
    }
};
```

## Test Cases
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total money you can rob = 1 + 3 = 4.
```

## Key Takeaways
- The dynamic programming approach allows for efficient computation of the maximum amount of money that can be robbed.
- The use of two separate arrays to track the maximum amount of money that can be robbed up to each house, with and without robbing the previous house, simplifies the decision-making process at each step.