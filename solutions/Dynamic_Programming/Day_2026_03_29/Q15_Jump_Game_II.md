# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. The function should return the minimum number of jumps to reach the last index. If it's impossible to reach the last index, return -1. The array can contain zeros, but you cannot jump from an index with a value of zero. For example, given the array [2,3,1,1,4], the output should be 2, because the optimal jump sequence is jump 1 step from index 0 to index 1, then 3 steps from index 1 to index 4.

## Approach
This problem can be solved using dynamic programming and greedy approach. The idea is to maintain an array to store the minimum number of jumps to reach each index. We can use a greedy approach to always try to extend the farthest reachable position.

## Complexity
- Time: O(n)
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
```

## Key Takeaways
- We use a greedy approach to always try to extend the farthest reachable position.
- We maintain two variables, maxReach and step, to track the farthest reachable position and the remaining steps before we need to make another jump.
- The time complexity is O(n) because we only need to traverse the array once.