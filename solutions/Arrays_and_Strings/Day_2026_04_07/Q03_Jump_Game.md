# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given the array `[2,3,1,1,4]`, you can reach the last index because you can jump from index 0 to index 1, then from index 1 to index 2, and so on. However, given the array `[3,2,1,0,4]`, you cannot reach the last index because you cannot jump from index 3 to index 4.

## Approach
The algorithm uses a greedy approach to track the maximum reachable position. It iterates through the array, updating the maximum reachable position at each step. If the maximum reachable position is ever less than the current index, it means we cannot reach the current index, and thus we cannot reach the last index.

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
            // if maxReach is less than i, it means we cannot reach this index
            if (maxReach < i) {
                return false;
            }
            // update maxReach
            maxReach = max(maxReach, i + nums[i]);
        }
        // if we can reach the last index, return true
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
- Use a greedy approach to solve the problem efficiently.
- Keep track of the maximum reachable position at each step.
- If the maximum reachable position is ever less than the current index, return false.