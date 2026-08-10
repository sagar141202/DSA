# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given the array `[2,3,1,1,4]`, you can reach the last index because you can jump from index 0 to index 1, then from index 1 to index 2, and so on. However, given the array `[3,2,1,0,4]`, you cannot reach the last index because you cannot jump from index 3 to index 4.

## Approach
The algorithm uses a greedy approach, iterating through the array and keeping track of the maximum reachable index. If the maximum reachable index is greater than or equal to the current index, we can continue iterating. The algorithm returns true if we can reach the last index and false otherwise.

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
            // If we cannot reach the current index, return false
            if (i > maxReach) {
                return false;
            }
            // Update the maximum reachable index
            maxReach = max(maxReach, i + nums[i]);
        }
        // If we can reach the last index, return true
        return true;
    }
};
```

## Test Cases
```
Input: [2,3,1,1,4]
Output: true
Input: [3,2,1,0,4]
Output: false
```

## Key Takeaways
- The greedy approach is suitable for this problem because we only need to keep track of the maximum reachable index.
- The time complexity is O(n) because we only iterate through the array once.
- The space complexity is O(1) because we only use a constant amount of space to store the maximum reachable index.