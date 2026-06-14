# Burst Balloons

## Problem Statement
Given a list of integers representing the coins you get when you burst a balloon, find the maximum coins you can collect. When you burst a balloon, the balloons on either side of it (if any) will be considered as having a balloon to their left and right respectively. The input list will have at least one element and at most 100 elements. Each element in the list will be between 1 and 100. For example, if the input is [3,1,5,8], the maximum coins you can collect is 167 (3*1*5 + 3*1*8 + 1*5*8 + 3*5*8).

## Approach
This problem can be solved using dynamic programming, where we build up a 2D table to store the maximum coins we can collect for each subproblem. The key observation is that when we burst a balloon, we need to consider the maximum coins we can collect from the left and right subproblems. We can use a recursive approach with memoization to solve this problem.

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
        vector<int> new_nums = {1};
        for (int num : nums) {
            new_nums.push_back(num);
        }
        new_nums.push_back(1);
        n += 2;
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int len = 1; len <= n - 1; len++) {
            for (int left = 0; left <= n - len - 1; left++) {
                int right = left + len;
                for (int i = left + 1; i < right; i++) {
                    dp[left][right] = max(dp[left][right], new_nums[left] * new_nums[i] * new_nums[right] + dp[left][i] + dp[i][right]);
                }
            }
        }
        return dp[0][n - 1];
    }
};

int main() {
    Solution solution;
    vector<int> nums = {3, 1, 5, 8};
    cout << solution.maxCoins(nums) << endl;
    return 0;
}
```

## Test Cases
```
Input: [3,1,5,8]
Output: 167
```

## Key Takeaways
- The key observation is that when we burst a balloon, we need to consider the maximum coins we can collect from the left and right subproblems.
- We can use a recursive approach with memoization to solve this problem, and build up a 2D table to store the maximum coins we can collect for each subproblem.
- The time complexity is O(n^3) and the space complexity is O(n^2), where n is the number of balloons.