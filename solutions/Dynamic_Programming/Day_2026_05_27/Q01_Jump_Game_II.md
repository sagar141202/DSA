# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. You are allowed to jump to any index within your jump range. For example, if you are at index 0 and the value at index 0 is 3, you can jump to any index from 1 to 3. If it is impossible to reach the last index, return -1.

## Approach
The approach to solve this problem is to use dynamic programming and greedy strategy. We will maintain an array to store the minimum number of jumps required to reach each index. We will iterate through the array and update the minimum number of jumps required to reach each index.

## Complexity
- Time: O(n^2)
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
Input: [2,3,1,1,4]
Output: 2
Input: [2,3,0,1,4]
Output: 2
```

## Key Takeaways
- The key to solving this problem is to maintain the maximum reachable index and the remaining steps before we need to make another jump.
- We use a greedy strategy to always try to reach the maximum reachable index.
- If we cannot reach the last index, we return -1.