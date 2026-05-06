# Combination Sum II

## Problem Statement
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate number is greater than the previous number and the sum of the numbers in the combination equals to the target. The same number may not be used more than once in the combination. The solution set must not contain duplicate combinations. For example, given candidates = [10,1,2,7,6,1,5] and target = 8, the output should be [[1,1,6],[1,2,5],[1,7],[2,6]].

## Approach
The solution uses recursion and backtracking to generate all combinations of the candidate numbers that sum to the target. It sorts the candidate numbers to ensure that each combination is unique. The algorithm iterates over the candidate numbers, adds each number to the current combination, and recursively generates all combinations that include the current number.

## Complexity
- Time: O(2^n) where n is the number of candidate numbers
- Space: O(n) for the recursion stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        // Sort the candidate numbers to ensure uniqueness
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> result;
        vector<int> current;
        backtrack(result, current, candidates, target, 0);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& candidates, int target, int start) {
        if (target == 0) {
            // Found a valid combination, add it to the result
            result.push_back(current);
            return;
        }
        for (int i = start; i < candidates.size(); i++) {
            // Skip duplicates to ensure uniqueness
            if (i > start && candidates[i] == candidates[i - 1]) continue;
            // Check if the current number exceeds the target
            if (candidates[i] > target) break;
            // Add the current number to the current combination
            current.push_back(candidates[i]);
            // Recursively generate combinations that include the current number
            backtrack(result, current, candidates, target - candidates[i], i + 1);
            // Backtrack by removing the current number from the current combination
            current.pop_back();
        }
    }
};

## Test Cases
```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
```

## Key Takeaways
- Use recursion and backtracking to generate all combinations of the candidate numbers.
- Sort the candidate numbers to ensure uniqueness and skip duplicates during the backtracking process.
- Check if the current number exceeds the target to prune the search space and improve efficiency.