# House Robber

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money in each house, return the maximum amount of money you can rob.

## Approach
The problem can be solved using dynamic programming, where we maintain two variables to track the maximum amount of money that can be robbed up to the current house and the previous house. We iterate through the array, at each step updating these variables based on whether we rob the current house or not. The maximum amount of money that can be robbed is the maximum of the two variables at the end.

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
        // base case: if there are no houses, we can't rob anything
        if (nums.empty()) return 0;
        
        // base case: if there is only one house, we can rob it
        if (nums.size() == 1) return nums[0];
        
        // initialize variables to track the maximum amount of money that can be robbed
        int prev = nums[0], curr = max(nums[0], nums[1]);
        
        // iterate through the array starting from the third house
        for (int i = 2; i < nums.size(); i++) {
            // update the variables based on whether we rob the current house or not
            int temp = curr;
            curr = max(curr, prev + nums[i]);
            prev = temp;
        }
        
        // the maximum amount of money that can be robbed is the maximum of the two variables
        return curr;
    }
};
```

## Test Cases
```
Input: nums = [1,2,3,1]
Output: 4
Input: nums = [2,7,9,3,1]
Output: 12
```

## Key Takeaways
- The problem can be solved using dynamic programming with a time complexity of O(n) and a space complexity of O(1).
- We need to consider the constraint that adjacent houses cannot be robbed on the same night.
- The solution involves maintaining variables to track the maximum amount of money that can be robbed up to the current house and the previous house.