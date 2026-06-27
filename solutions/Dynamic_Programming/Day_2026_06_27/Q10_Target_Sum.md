# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets that sum up to the target sum. The array can contain both positive and negative integers. The problem can be formalized as follows: given an array `nums` and a target sum `S`, find the number of subsets of `nums` that sum up to `S`. The constraints are: `1 <= nums.length <= 20`, `-10^6 <= nums[i] <= 10^6`, and `0 <= S <= 10^6`.

## Approach
The problem can be solved using dynamic programming, where we build up a table to store the number of subsets that sum up to each possible sum from 0 to the target sum. The key insight is to use a recursive approach with memoization to avoid redundant calculations. We can iterate over the array and for each element, we have two choices: include it in the subset or exclude it.

## Complexity
- Time: O(2^n * S)
- Space: O(n * S)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int n = nums.size();
        // Create a dp table to store the number of subsets that sum up to each possible sum
        unordered_map<int, int> dp;
        dp[0] = 1;
        
        for (int i = 0; i < n; i++) {
            unordered_map<int, int> temp;
            for (auto& x : dp) {
                // For each possible sum, we have two choices: include the current element or exclude it
                temp[x.first + nums[i]] += x.second;
                temp[x.first - nums[i]] += x.second;
            }
            dp = temp;
        }
        
        // Return the number of subsets that sum up to the target sum
        return dp.count(S) ? dp[S] : 0;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 1, 1, 1, 1};
    int S = 3;
    cout << solution.findTargetSumWays(nums, S) << endl;
    return 0;
}
```

## Test Cases
```
Input: nums = [1, 1, 1, 1, 1], S = 3
Output: 5
```

## Key Takeaways
- The problem can be solved using dynamic programming with a recursive approach and memoization.
- The time complexity is O(2^n * S) due to the recursive nature of the solution and the need to iterate over all possible sums.
- The space complexity is O(n * S) due to the need to store the dp table.