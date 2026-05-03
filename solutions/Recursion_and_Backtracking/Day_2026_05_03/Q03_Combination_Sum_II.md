# Combination Sum II

## Problem Statement
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate number is greater than the previous number in the combination, and the sum of the combination is equal to the target. Each number in candidates may only be used once in the combination. The solution set must not contain duplicate combinations. The candidates array is not sorted, and the target is a positive integer. For example, if candidates = [10,1,2,7,6,1,5] and target = 8, then the output should be [[1,1,6],[1,2,5],[1,7],[2,6]].

## Approach
The problem can be solved using recursion and backtracking to generate all possible combinations. We will iterate through the candidates array, adding each candidate to the current combination and recursively calling the function with the remaining target. If the target becomes zero, it means we have found a valid combination.

## Complexity
- Time: O(2^n) where n is the number of candidates, as in the worst case we might have to generate all possible combinations.
- Space: O(n) for the recursion stack, where n is the number of candidates.

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
```

## Key Takeaways
- Use recursion and backtracking to generate all possible combinations.
- Sort the candidates array to handle duplicate combinations.
- Skip duplicates to ensure unique combinations.