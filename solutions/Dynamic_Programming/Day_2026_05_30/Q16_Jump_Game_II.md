# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. You are not allowed to jump out of the bounds of the array. If it is impossible to reach the last index, return -1. For example, given the array [2,3,1,1,4], the minimum number of jumps to reach the last index is 2 (jump 1 step from index 0 to index 1, then 3 steps to index 4).

## Approach
The approach to this problem involves using dynamic programming to keep track of the minimum number of jumps required to reach each index. We use a greedy strategy to always choose the index that allows us to jump the farthest. The algorithm iterates over the array, updating the minimum number of jumps required to reach each index.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;
        
        int maxReach = nums[0];
        int step = nums[0];
        int jumps = 1;
        
        for (int i = 1; i < n; i++) {
            if (i == n - 1) return jumps;
            
            maxReach = max(maxReach, i + nums[i]);
            step--;
            
            if (step == 0) {
                jumps++;
                if (i >= maxReach) return -1;
                step = maxReach - i;
            }
        }
        
        return -1;
    }
};
```

## Test Cases
```
Input: [2,3,1,1,4]
Output: 2
Input: [2,3,0,1,4]
Output: 2
Input: [0,1,2,3,4]
Output: -1
```

## Key Takeaways
- We use a greedy strategy to always choose the index that allows us to jump the farthest.
- We keep track of the maximum reachable index and the number of steps remaining before we need to make another jump.
- If we reach a point where we cannot make another jump, we return -1 to indicate that it is impossible to reach the last index.