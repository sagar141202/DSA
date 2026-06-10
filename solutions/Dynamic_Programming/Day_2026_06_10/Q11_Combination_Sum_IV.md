# Combination Sum IV

## Problem Statement
Given an array of distinct integers `candidates` and a target integer `target`, return the number of combinations that sum up to `target`. The same number may be used an unlimited number of times. You can assume that the input array `candidates` contains at least one positive integer and that the target `target` is always positive. For example, if `candidates = [1, 2, 3]` and `target = 4`, then the possible combinations are `(1, 1, 1, 1)`, `(1, 1, 2)`, `(1, 3)`, and `(2, 2)`, so the output should be `4`.

## Approach
We use dynamic programming to solve this problem by maintaining an array `dp` where `dp[i]` represents the number of combinations that sum up to `i`. We initialize `dp[0] = 1` and then iterate through each number from `1` to `target`, updating `dp[i]` by adding the number of combinations that sum up to `i - candidate` for each `candidate` in the `candidates` array.

## Complexity
- Time: O(target * n)
- Space: O(target)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int combinationSum4(vector<int>& candidates, int target) {
        // Create a dynamic programming array
        vector<int> dp(target + 1, 0);
        
        // Base case: there is one way to sum up to 0
        dp[0] = 1;
        
        // Iterate through each number from 1 to target
        for (int i = 1; i <= target; i++) {
            // Iterate through each candidate
            for (int candidate : candidates) {
                // If the current number is greater than or equal to the candidate
                if (i >= candidate) {
                    // Update dp[i] by adding the number of combinations that sum up to i - candidate
                    dp[i] += dp[i - candidate];
                }
            }
        }
        
        // Return the number of combinations that sum up to target
        return dp[target];
    }
};
```

## Test Cases
```
Input: candidates = [1, 2, 3], target = 4
Output: 7
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems.
- Initialize the base case carefully to ensure the correctness of the solution.
- The time complexity is O(target * n) because we iterate through each number from 1 to target and each candidate in the candidates array.