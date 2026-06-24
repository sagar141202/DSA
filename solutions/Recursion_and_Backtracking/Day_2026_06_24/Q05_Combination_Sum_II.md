# Combination Sum II

## Problem Statement
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate number is greater than the previous number and the sum of the combination is equal to the target. Each number in candidates may only be used once in the combination. The solution set must not contain duplicate combinations. For example, if the input is candidates = [10,1,2,7,6,1,5] and target = 8, then the output is [[1,1,6],[1,2,5],[1,7],[2,6]].

## Approach
The problem can be solved using recursion and backtracking, where we try to add each candidate number to the current combination and recursively call the function with the updated target and combination. We use backtracking to remove the last added number when the current combination's sum exceeds the target.

## Complexity
- Time: O(2^n) where n is the number of candidates, due to the recursive nature of the solution
- Space: O(n) for the recursive call stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(int remain, vector<int>& comb, int start, vector<int>& candidates, vector<vector<int>>& result) {
    if (remain == 0) {
        result.push_back(comb);
        return;
    } else if (remain < 0) {
        return;
    }
    for (int i = start; i < candidates.size(); i++) {
        // Skip duplicates to ensure unique combinations
        if (i > start && candidates[i] == candidates[i-1]) continue;
        comb.push_back(candidates[i]);
        backtrack(remain - candidates[i], comb, i + 1, candidates, result);
        comb.pop_back();
    }
}

vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    vector<vector<int>> result;
    vector<int> comb;
    sort(candidates.begin(), candidates.end());
    backtrack(target, comb, 0, candidates, result);
    return result;
}
```

## Test Cases
```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
Input: candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]
```

## Key Takeaways
- Use recursion and backtracking to explore all possible combinations of candidate numbers.
- Sort the candidate numbers to easily skip duplicates and ensure unique combinations.
- Use a start index to keep track of the current position in the candidate array and avoid using the same number multiple times in a combination.