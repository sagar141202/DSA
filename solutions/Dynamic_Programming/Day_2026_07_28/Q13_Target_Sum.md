# Target Sum

## Problem Statement
Given an array of integers and a target sum, find the number of subsets that sum up to the target sum. The array can contain both positive and negative integers. The problem can be formally stated as: given an array `arr` of size `n` and a target sum `target`, find the number of subsets of `arr` that sum up to `target`. The constraints are: `1 <= n <= 1000`, `-10^5 <= arr[i] <= 10^5`, and `-10^5 <= target <= 10^5`.

## Approach
The problem can be solved using dynamic programming by creating a 2D table where each cell represents the number of subsets that sum up to a certain value. The algorithm builds up the table iteratively, considering each element in the array and updating the table accordingly. This approach ensures that all possible subsets are considered and counted correctly.

## Complexity
- Time: O(n * target)
- Space: O(n * target)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findTargetSumWays(vector<int>& nums, int target) {
    int n = nums.size();
    int sum = 0;
    for (int num : nums) sum += num;
    
    // If the target sum is greater than the sum of all elements or less than the negative sum of all elements, return 0
    if (abs(target) > sum) return 0;
    
    // Create a 2D table to store the number of subsets that sum up to each value
    int dp[n + 1][2 * sum + 1] = {0};
    
    // Initialize the base case where the sum is 0
    dp[0][sum] = 1;
    
    // Iterate over each element in the array
    for (int i = 1; i <= n; i++) {
        // Iterate over each possible sum
        for (int j = 0; j <= 2 * sum; j++) {
            // If the current sum is achievable, update the table accordingly
            if (j - nums[i - 1] >= 0) dp[i][j] += dp[i - 1][j - nums[i - 1]];
            if (j + nums[i - 1] <= 2 * sum) dp[i][j] += dp[i - 1][j + nums[i - 1]];
        }
    }
    
    // Return the number of subsets that sum up to the target sum
    return dp[n][sum + target];
}
```

## Test Cases
```
Input: nums = [1, 1, 1, 1, 1], target = 3
Output: 5
Input: nums = [1], target = 1
Output: 1
```

## Key Takeaways
- Dynamic programming can be used to solve problems that have overlapping subproblems and optimal substructure.
- The 2D table is used to store the number of subsets that sum up to each value, allowing us to avoid redundant calculations and improve efficiency.
- The algorithm iterates over each element in the array and updates the table accordingly, ensuring that all possible subsets are considered and counted correctly.