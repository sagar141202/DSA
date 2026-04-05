# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. If it's impossible to reach the last index, return -1. For example, given the array `[2,3,1,1,4]`, the minimum number of jumps to reach the last index is `2` (jump 1 step from index 0 to index 1, then 3 steps to index 4). The constraints are: `1 <= nums.length <= 1000`, `0 <= nums[i] <= 10^5`.

## Approach
The algorithm uses dynamic programming to track the minimum number of jumps to reach each index. We iterate over the array and for each index, we check the minimum number of jumps to reach it. The dynamic programming approach helps us avoid redundant calculations and find the optimal solution efficiently. We use a greedy strategy to always choose the index that allows us to jump the farthest.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
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
- Use dynamic programming to track the minimum number of jumps to reach each index.
- Always choose the index that allows us to jump the farthest using a greedy strategy.
- Handle edge cases where it's impossible to reach the last index.