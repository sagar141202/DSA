# Combination Sum II

## Problem Statement
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate number is greater than the previous number and the sum of the combination is equal to the target. The same number may not be used more than once in the combination. Return a list of all unique combinations.

## Approach
The problem can be solved using recursion and backtracking. We will sort the candidates array and then use a recursive function to find all combinations that sum up to the target. We will use a backtrack function to explore all possible combinations.

## Complexity
- Time: O(2^n) where n is the number of candidates
- Space: O(n) for the recursion stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& candidates, int start, int target, vector<int>& path, vector<vector<int>>& result) {
    if (target < 0) return;
    if (target == 0) {
        result.push_back(path);
        return;
    }
    for (int i = start; i < candidates.size(); i++) {
        // skip duplicates
        if (i > start && candidates[i] == candidates[i-1]) continue;
        path.push_back(candidates[i]);
        backtrack(candidates, i + 1, target - candidates[i], path, result);
        path.pop_back();
    }
}

vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    vector<vector<int>> result;
    vector<int> path;
    sort(candidates.begin(), candidates.end());
    backtrack(candidates, 0, target, path, result);
    return result;
}
```

## Test Cases
```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
```

## Key Takeaways
- Use recursion and backtracking to solve problems that require exploring all possible combinations.
- Sort the input array to handle duplicates and improve efficiency.
- Use a backtrack function to explore all possible combinations and avoid duplicates.