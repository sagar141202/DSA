# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given the array `[2,3,1,1,4]`, you can reach the last index because you can jump from index 0 to index 1, then from index 1 to index 2, and so on. However, given the array `[3,2,1,0,4]`, you cannot reach the last index.

## Approach
The algorithm uses a greedy approach to track the maximum reachable position. It iterates through the array, updating the maximum reachable position at each step. If the current position is beyond the maximum reachable position, it returns false. The intuition is to always try to extend the maximum reachable position as far as possible.

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
        // Initialize the maximum reachable position
        int maxReach = 0;
        
        // Iterate through the array
        for (int i = 0; i < nums.size(); i++) {
            // If the current position is beyond the maximum reachable position, return false
            if (i > maxReach) {
                return false;
            }
            // Update the maximum reachable position
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
- We use a greedy approach to track the maximum reachable position.
- We iterate through the array only once, resulting in a time complexity of O(n).
- We use a constant amount of space to store the maximum reachable position, resulting in a space complexity of O(1).