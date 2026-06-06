# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. If it is impossible to reach the last index, return 0. The array is 0-indexed, and you can only jump to indices within the bounds of the array. For example, given the array [2,3,1,1,4], the minimum number of jumps to reach the last index is 2 (0 -> 1 -> 4).

## Approach
The problem can be solved using dynamic programming and greedy approach. We maintain an array to store the minimum number of jumps to reach each index. At each index, we try to extend the range of the current index by checking all previous indices that can reach the current index.

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
                if (i >= maxReach) return -1; // or throw an exception
                step = maxReach - i;
            }
        }
        return -1; // or throw an exception
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
- Use dynamic programming and greedy approach to solve the problem efficiently.
- Maintain variables to track the maximum reachable index and the remaining steps before the next jump.
- Handle edge cases where it is impossible to reach the last index.