# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. You are not allowed to jump out of the array bounds. For example, if the input array is [2,3,1,1,4], the minimum number of jumps to reach the last index is 2 (0 -> 1 -> 4).

## Approach
The problem can be solved using dynamic programming by maintaining an array to store the minimum number of jumps required to reach each index. We iterate through the array and update the minimum number of jumps required to reach each index based on the previous indices that can jump to it. The algorithm uses a greedy approach to always choose the index that can jump to the farthest position.

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
- Use dynamic programming to solve the problem by maintaining an array to store the minimum number of jumps required to reach each index.
- Use a greedy approach to always choose the index that can jump to the farthest position.
- The time complexity of the solution is O(n) and the space complexity is O(1), making it efficient for large inputs.