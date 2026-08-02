# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of ways to assign + or - sign to each integer in the array such that the sum of all integers equals the target sum. The array can contain duplicate integers and the target sum can be any integer. For example, given the array [1, 1, 1, 1, 1] and the target sum 3, there are 5 ways to achieve the target sum: [1, 1, 1, -1, -1], [1, 1, -1, 1, -1], [1, -1, 1, 1, -1], [-1, 1, 1, 1, -1], and [1, -1, -1, 1, 1].

## Approach
The problem can be solved using dynamic programming, where we build up a table of solutions for subproblems. We use a recursive approach with memoization to store the results of subproblems. The base case is when the sum equals the target sum.

## Complexity
- Time: O(n * sum)
- Space: O(n * sum)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findTargetSumWays(vector<int>& nums, int target) {
    int sum = accumulate(nums.begin(), nums.end(), 0);
    if (sum < abs(target) || (sum + target) % 2 != 0) return 0;
    int s = (sum + target) / 2;
    vector<int> dp(s + 1, 0);
    dp[0] = 1;
    for (int num : nums) {
        for (int i = s; i >= num; --i) {
            dp[i] += dp[i - num];
        }
    }
    return dp[s];
}

int main() {
    vector<int> nums = {1, 1, 1, 1, 1};
    int target = 3;
    cout << findTargetSumWays(nums, target) << endl;
    return 0;
}
```

## Test Cases
```
Input: nums = [1, 1, 1, 1, 1], target = 3
Output: 5
Input: nums = [1], target = 1
Output: 1
Input: nums = [1, 0], target = 1
Output: 2
```

## Key Takeaways
- Use dynamic programming to solve the problem by building up a table of solutions for subproblems.
- Use a recursive approach with memoization to store the results of subproblems.
- The base case is when the sum equals the target sum, and we can use this to terminate the recursion.