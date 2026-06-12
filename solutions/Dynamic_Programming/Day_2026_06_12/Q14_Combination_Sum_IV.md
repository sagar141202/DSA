# Combination Sum IV

## Problem Statement
Given an array of distinct integers `candidates` and a target integer `target`, return the number of combinations that sum up to `target`. Each number in `candidates` may be used an unlimited number of times in the combination. The solution should be able to handle large inputs and should not use recursion.

## Approach
The problem can be solved using dynamic programming, where we build up a table of combinations for each number up to the target. We iterate over each candidate and update the table accordingly. The final result is stored in the last entry of the table.

## Complexity
- Time: O(target * n) where n is the number of candidates
- Space: O(target)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int combinationSum4(vector<int>& candidates, int target) {
        // Create a dynamic programming table
        vector<int> dp(target + 1, 0);
        dp[0] = 1;  // base case: one way to sum up to 0
        
        // Fill up the table
        for (int i = 1; i <= target; i++) {
            for (int candidate : candidates) {
                if (i - candidate >= 0) {
                    dp[i] += dp[i - candidate];
                }
            }
        }
        
        return dp[target];
    }
};
```

## Test Cases
```
Input: candidates = [1, 2, 3], target = 4
Output: 7
Explanation: The possible combinations are:
1 + 1 + 1 + 1
1 + 1 + 2
1 + 2 + 1
1 + 3
2 + 1 + 1
2 + 2
3 + 1
```

## Key Takeaways
- Dynamic programming can be used to solve problems with overlapping subproblems.
- The problem can be broken down into smaller subproblems and solved iteratively.
- The use of a table to store intermediate results can help avoid redundant calculations and improve efficiency.