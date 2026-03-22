# House Robber

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police. The constraints are: `1 <= nums.length <= 100`, `0 <= nums[i] <= 1000`.

## Approach
This problem can be solved using Dynamic Programming by maintaining two variables to track the maximum amount of money that can be robbed up to the current house and the house before it. The algorithm iterates through the houses, updating these variables based on whether the current house is robbed or not. The maximum amount of money that can be robbed is the maximum of these two variables at the last house.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        if (nums.size() == 1) return nums[0];
        
        int prev = nums[0];
        int curr = max(nums[0], nums[1]);
        
        for (int i = 2; i < nums.size(); i++) {
            int temp = curr;
            curr = max(curr, prev + nums[i]);
            prev = temp;
        }
        
        return curr;
    }
};
```

## Test Cases
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total money you can rob = 1 + 3 = 4.
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total money you can rob = 2 + 9 + 1 = 12.
```

## Key Takeaways
- The problem can be solved using a bottom-up dynamic programming approach with a time complexity of O(n) and a space complexity of O(1).
- The key insight is to maintain two variables to track the maximum amount of money that can be robbed up to the current house and the house before it.
- The algorithm can be optimized by using a constant amount of space to store the previous two houses' maximum amounts.