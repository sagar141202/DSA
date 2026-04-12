# Combination Sum II

## Problem Statement
Given a collection of candidate numbers and a target number, find all unique combinations in the collection where the candidate numbers sum to the target. Each number in the collection may only be used once in the combination. The solution set must not contain duplicate combinations. For example, given candidate set [10,1,2,7,6,1,5] and target 8, one of the possible output is [1,1,6], [1,2,5], [1,7], [2,6].

## Approach
The algorithm uses backtracking to find all combinations that sum to the target. It iterates over the candidates, adds each to the current combination, and recursively checks if the remaining sum can be reached. If the sum is reached, the combination is added to the result. The algorithm skips duplicate candidates to avoid duplicate combinations.

## Complexity
- Time: O(2^n) where n is the number of candidates, due to the recursive backtracking.
- Space: O(n) for the recursive call stack and storing the combinations.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& candidates, int target, int start, vector<int>& path, vector<vector<int>>& result) {
    if (target < 0) return; // sum exceeds target
    if (target == 0) {
        result.push_back(path); // valid combination found
        return;
    }
    for (int i = start; i < candidates.size(); i++) {
        if (i > start && candidates[i] == candidates[i-1]) continue; // skip duplicates
        path.push_back(candidates[i]);
        backtrack(candidates, target - candidates[i], i + 1, path, result);
        path.pop_back();
    }
}

vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    vector<vector<int>> result;
    vector<int> path;
    sort(candidates.begin(), candidates.end());
    backtrack(candidates, target, 0, path, result);
    return result;
}
```

## Test Cases
```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6], [1,2,5], [1,7], [2,6]]
```

## Key Takeaways
- Use backtracking to explore all possible combinations of candidates.
- Skip duplicate candidates to avoid duplicate combinations.
- Use a recursive approach to simplify the code and improve readability.