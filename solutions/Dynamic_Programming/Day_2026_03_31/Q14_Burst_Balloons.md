# Burst Balloons
## Problem Statement
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it, represented by an array nums. When we burst a balloon, we get the points from the product of the numbers on the balloons to the left and right of it. If there's no balloon to the left or right, the points are multiplied by 1. The goal is to find the maximum points we can get by bursting all the balloons.

## Approach
The problem can be solved using dynamic programming by considering each balloon as a potential last balloon to burst and calculating the maximum points for each subproblem. The algorithm involves iterating over all possible last balloons and using a 2D array to store the maximum points for subproblems. 

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        // Add 1 at the beginning and end to simplify the calculation
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        
        // Initialize a 2D array to store the maximum points for subproblems
        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
        
        // Iterate over all possible lengths of subproblems
        for (int length = 1; length <= n + 1; length++) {
            // Iterate over all possible start indices for subproblems
            for (int left = 0; left <= n + 1 - length; left++) {
                int right = left + length - 1;
                // Initialize the maximum points for the current subproblem
                for (int i = left; i <= right; i++) {
                    // Calculate the maximum points by considering the current balloon as the last one to burst
                    dp[left][right] = max(dp[left][right], nums[left - 1] * nums[i] * nums[right + 1] + dp[left][i - 1] + dp[i + 1][right]);
                }
            }
        }
        
        // Return the maximum points for the entire problem
        return dp[1][n];
    }
};

int main() {
    Solution solution;
    vector<int> nums = {3, 1, 5, 8};
    cout << "Maximum points: " << solution.maxCoins(nums) << endl;
    return 0;
}
```

## Test Cases
```
Input: nums = [3,1,5,8]
Output: 167
Input: nums = [1,5]
Output: 10
```

## Key Takeaways
- The dynamic programming approach is used to solve the problem by considering each balloon as a potential last balloon to burst.
- A 2D array is used to store the maximum points for subproblems, which helps to avoid redundant calculations and improve efficiency.
- The algorithm involves iterating over all possible lengths and start indices for subproblems, and calculating the maximum points by considering each balloon as the last one to burst.