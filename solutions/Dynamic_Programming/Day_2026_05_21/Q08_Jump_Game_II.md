# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. Assume that you can always reach the last index.

## Approach
We will use a dynamic programming approach to solve this problem, where we maintain an array to store the minimum number of jumps required to reach each index. We iterate through the array and update the minimum number of jumps for each index based on the previous indices that can reach it.

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
        
        return jumps;
    }
};
```

## Test Cases
```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. 
             One possible way is jump 1 step from index 0 to index 1, then 3 steps to index 4.
Input: nums = [2,3,0,1,4]
Output: 2
```

## Key Takeaways
- Use a greedy approach to find the minimum number of jumps.
- Maintain two variables, maxReach and step, to track the maximum reachable index and the remaining steps before we need to make another jump.
- Update maxReach and step at each index based on the current jump length and the remaining steps.