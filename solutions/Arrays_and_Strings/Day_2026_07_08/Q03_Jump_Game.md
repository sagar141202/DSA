# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given `nums = [2,3,1,1,4]`, the function should return `true` because we can reach the last index (4) from the first index (0) by the following sequence of jumps: 0 -> 1 -> 3 -> 4. However, given `nums = [3,2,1,0,4]`, the function should return `false` because there is no sequence of jumps that can reach the last index.

## Approach
The algorithm uses a greedy approach to track the maximum reachable position. It iterates through the array and updates the maximum reachable position at each step. If the current position is beyond the maximum reachable position, it returns false. The algorithm has a time complexity of O(n), where n is the number of elements in the array.

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
        int maxReach = 0;
        for (int i = 0; i < nums.size(); i++) {
            // if current position is beyond maxReach, return false
            if (i > maxReach) return false;
            // update maxReach
            maxReach = max(maxReach, i + nums[i]);
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
- The greedy approach can be used to solve this problem efficiently.
- Tracking the maximum reachable position is crucial to determining if the last index can be reached.
- The algorithm has a linear time complexity, making it suitable for large inputs.