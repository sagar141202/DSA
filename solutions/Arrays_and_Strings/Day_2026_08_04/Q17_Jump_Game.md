# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given `nums = [2,3,1,1,4]`, the function should return `true` because we can reach the last index (4) from the first index (0) by jumping to index 1 and then to the last index. On the other hand, given `nums = [3,2,1,0,4]`, the function should return `false` because we cannot reach the last index from the first index.

## Approach
The algorithm uses a greedy approach, keeping track of the maximum reachable position. It iterates over the array, updating the maximum reachable position if the current index is within the reachable range. If the current index exceeds the maximum reachable position, the function returns false, indicating that the last index cannot be reached.

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
            // if current index is beyond maxReach, return false
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
- The greedy approach is suitable for this problem because we only need to keep track of the maximum reachable position.
- The time complexity is linear, making it efficient for large inputs.
- The space complexity is constant, as we only use a fixed amount of space to store the maximum reachable position.