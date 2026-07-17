# Jump Game

## Problem Statement
Given an array of non-negative integers, where each element represents the maximum jump length from that position, determine if you are able to reach the last index. The function should return true if you can reach the last index, otherwise return false. The constraints are: 1 <= nums.length <= 10^4, 0 <= nums[i] <= 10^5.

## Approach
The algorithm uses a greedy approach to track the maximum reachable position. It iterates through the array, updating the maximum reachable position at each step. If the current position is beyond the maximum reachable position, the function returns false. The intuition is to always try to extend the maximum reachable position as far as possible.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxReach = 0; // maximum reachable position
        for (int i = 0; i < nums.size(); i++) {
            if (i > maxReach) return false; // if current position is beyond maxReach
            maxReach = max(maxReach, i + nums[i]); // update maxReach
        }
        return true;
    }
};
```

## Test Cases
```
Input: nums = [2,3,1,1,4]
Output: true
Input: nums = [3,2,1,0,4]
Output: false
```

## Key Takeaways
- The greedy approach is suitable for this problem because it allows us to make the locally optimal choice of extending the maximum reachable position at each step.
- The time complexity is O(n) because we only need to iterate through the array once.
- The space complexity is O(1) because we only use a constant amount of space to store the maximum reachable position.