# Combination Sum II

## Problem Statement
Given a collection of candidate numbers and a target number, find all unique combinations in the candidate numbers that sum up to the target number. Each number in the candidate numbers may only be used once in the combination. The solution set must not contain duplicate combinations. For example, given candidate set [10,1,2,7,6,1,5] and target 8, a solution set is [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]].

## Approach
The problem can be solved using recursion and backtracking. We will sort the candidate numbers and use a recursive function to find all combinations that sum up to the target number. We will also use a technique called pruning to avoid duplicate combinations.

## Complexity
- Time: O(2^n) where n is the number of candidate numbers
- Space: O(n) for the recursive call stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& candidates, int target, int start, vector<int>& path, vector<vector<int>>& result) {
    if (target < 0) return;
    if (target == 0) {
        result.push_back(path);
        return;
    }
    for (int i = start; i < candidates.size(); i++) {
        // skip duplicates
        if (i > start && candidates[i] == candidates[i-1]) continue;
        path.push_back(candidates[i]);
        backtrack(candidates, target - candidates[i], i + 1, path, result);
        path.pop_back();
    }
}

vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    sort(candidates.begin(), candidates.end());
    vector<vector<int>> result;
    vector<int> path;
    backtrack(candidates, target, 0, path, result);
    return result;
}
```

## Test Cases
```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
```

## Key Takeaways
- Use recursion and backtracking to solve the problem
- Sort the candidate numbers to avoid duplicate combinations
- Use a technique called pruning to avoid duplicate combinations by skipping duplicates in the recursive function.