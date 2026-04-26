# House Robber

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob.

## Approach
The problem can be solved using Dynamic Programming by maintaining two variables to track the maximum amount of money that can be robbed up to the current house and the maximum amount of money that can be robbed up to the previous house. The algorithm iterates through the array, updating these variables at each step.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.empty()) return 0;
        if (nums.size() == 1) return nums[0];
        
        // Initialize a vector to store the maximum amount of money that can be robbed up to each house
        vector<int> dp(nums.size());
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        
        // Iterate through the array, updating the dp vector at each step
        for (int i = 2; i < nums.size(); i++) {
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        }
        
        // The maximum amount of money that can be robbed is stored in the last element of the dp vector
        return dp.back();
    }
};
```

## Test Cases
```
Input: nums = [1,2,3,1]
Output: 4
Input: nums = [2,7,9,3,1]
Output: 12
```

## Key Takeaways
- The problem can be solved using Dynamic Programming by maintaining a vector to track the maximum amount of money that can be robbed up to each house.
- The time complexity is O(n), where n is the number of houses, and the space complexity is O(n) due to the use of the dp vector.
- The solution involves iterating through the array and updating the dp vector at each step to find the maximum amount of money that can be robbed.