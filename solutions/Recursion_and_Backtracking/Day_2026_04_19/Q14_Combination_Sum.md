# Combination Sum

## Problem Statement
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations in `candidates` where the candidate numbers sum to `target`. The same number may be used an unlimited number of times. The solution should be in a form of a list of lists, where each sublist is a combination that sums up to the target.

## Approach
The problem can be solved using recursion and backtracking. We start by iterating over the candidates array and for each candidate, we recursively call the function with the remaining target and the current combination. If the remaining target is zero, we have found a valid combination. The algorithm will explore all possible combinations and return the ones that sum up to the target.

## Complexity
- Time: O(N^(T/M + 1)) where N is the number of candidates, T is the target, and M is the minimum value among the candidates.
- Space: O(T/M) for the recursion stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        // Sort the candidates array to make the solution more efficient
        sort(candidates.begin(), candidates.end());
        
        vector<vector<int>> result;
        vector<int> currentCombination;
        
        // Recursive function to find combinations
        backtrack(result, currentCombination, candidates, target, 0);
        
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& currentCombination, vector<int>& candidates, int remainingTarget, int startIndex) {
        // If the remaining target is zero, we have found a valid combination
        if (remainingTarget == 0) {
            result.push_back(currentCombination);
            return;
        }
        
        // Iterate over the candidates array starting from the startIndex
        for (int i = startIndex; i < candidates.size(); i++) {
            // If the current candidate is greater than the remaining target, break the loop
            if (candidates[i] > remainingTarget) {
                break;
            }
            
            // Add the current candidate to the current combination
            currentCombination.push_back(candidates[i]);
            
            // Recursively call the backtrack function with the updated remaining target and the current combination
            backtrack(result, currentCombination, candidates, remainingTarget - candidates[i], i);
            
            // Remove the last added candidate from the current combination (backtracking)
            currentCombination.pop_back();
        }
    }
};
```

## Test Cases
```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Input: candidates = [2], target = 1
Output: []
```

## Key Takeaways
- Use recursion and backtracking to solve problems that require exploring all possible combinations.
- Sort the input array to make the solution more efficient.
- Use a recursive function to explore all possible combinations and add valid combinations to the result list.