# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. You are allowed to jump to any index within your jump range. For example, if you are at index 0 and the value at index 0 is 3, you can jump to index 1, 2, or 3. If it is not possible to reach the last index, return -1.

## Approach
We will use dynamic programming to solve this problem. The idea is to maintain an array where each element represents the minimum number of jumps required to reach that index. We will iterate over the array and update the minimum number of jumps for each index.

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

int main() {
    Solution solution;
    vector<int> nums = {2, 3, 1, 1, 4};
    cout << solution.jump(nums) << endl;
    return 0;
}
```

## Test Cases
```
Input: [2, 3, 1, 1, 4]
Output: 2
Input: [2, 3, 0, 1, 4]
Output: 2
Input: [0, 1, 2, 3, 4]
Output: -1
```

## Key Takeaways
- The dynamic programming approach helps to avoid redundant calculations and reduce the time complexity.
- The use of two pointers, maxReach and step, helps to track the maximum reachable index and the number of steps remaining before we need to make another jump.
- The algorithm returns -1 if it is not possible to reach the last index.