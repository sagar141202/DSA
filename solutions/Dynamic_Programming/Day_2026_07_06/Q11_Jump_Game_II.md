# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. If it is impossible to reach the last index, return -1. The array is 0-indexed, and you can only jump to indices within the bounds of the array. For example, given the array [2,3,1,1,4], the minimum number of jumps to reach the last index is 2 (jump 1 step from index 0 to index 1, then 3 steps to index 4).

## Approach
We use dynamic programming to solve this problem by maintaining an array to store the minimum number of jumps required to reach each index. We iterate over the array, updating the minimum number of jumps for each index based on the minimum number of jumps required to reach the previous indices that can jump to the current index.

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
        
        return -1; // should not reach here
    }
};
```

## Test Cases
```
Input: [2,3,1,1,4]
Output: 2
Input: [2,3,0,1,4]
Output: 2
```

## Key Takeaways
- We maintain two variables, `maxReach` and `step`, to keep track of the maximum reachable index and the remaining steps before we need to make another jump.
- We update `maxReach` and `step` as we iterate through the array, and increment the `jumps` counter whenever we need to make another jump.
- The time complexity is O(n) because we only need to iterate through the array once, and the space complexity is O(1) because we only use a constant amount of space to store our variables.