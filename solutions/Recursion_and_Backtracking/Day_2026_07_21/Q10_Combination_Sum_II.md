# Combination Sum II

## Problem Statement
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations in `candidates` where the candidate numbers sum to `target`. The same number may not be used unlimited times in a combination, but each number may be used only as many times as it appears in `candidates`. The combinations should be sorted in ascending order, and each combination should be in non-descending sort order.

## Approach
The problem can be solved using recursion and backtracking, where we explore all possible combinations and backtrack when the sum exceeds the target. We will use a helper function to perform the recursion and backtracking. The base case for the recursion will be when the remaining sum is zero, at which point we add the current combination to the result.

## Complexity
- Time: O(2^n * n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        // Sort the candidates array
        sort(candidates.begin(), candidates.end());
        
        // Initialize the result vector
        vector<vector<int>> result;
        
        // Define a helper function for recursion and backtracking
        vector<int> current;
        function<void(int, int, int)> backtrack = [&](int start, int remaining, int lastUsed) {
            // Base case: when the remaining sum is zero
            if (remaining == 0) {
                result.push_back(current);
                return;
            }
            
            // Explore all possible combinations
            for (int i = start; i < candidates.size(); i++) {
                // Skip duplicates to ensure uniqueness
                if (i > start && candidates[i] == candidates[i - 1]) {
                    continue;
                }
                
                // Check if the current number exceeds the remaining sum
                if (candidates[i] > remaining) {
                    break;
                }
                
                // Add the current number to the current combination
                current.push_back(candidates[i]);
                
                // Recur for the next number
                backtrack(i + 1, remaining - candidates[i], candidates[i]);
                
                // Backtrack by removing the last added number
                current.pop_back();
            }
        };
        
        // Start the recursion and backtracking
        backtrack(0, target, INT_MIN);
        
        // Return the result
        return result;
    }
};
```

## Test Cases
```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
```

## Key Takeaways
- Use recursion and backtracking to explore all possible combinations.
- Sort the candidates array to ensure non-descending order and to skip duplicates.
- Use a helper function to perform the recursion and backtracking, and define the base case for the recursion.