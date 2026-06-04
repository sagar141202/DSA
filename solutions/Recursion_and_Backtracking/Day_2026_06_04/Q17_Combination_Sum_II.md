# Combination Sum II

## Problem Statement
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate number is greater than the previous number and the sum of the combination equals to target. Each number in candidates may only be used once in the combination. The solution set must not contain duplicate combinations.

## Approach
The problem can be solved using recursion and backtracking. We start by sorting the candidates array and then recursively try to add each candidate to the current combination. If the sum of the current combination exceeds the target, we backtrack and try the next candidate. We also skip duplicate combinations by checking if the current candidate is the same as the previous one.

## Complexity
- Time: O(2^n) where n is the number of candidates, as in the worst case we have to try all possible combinations.
- Space: O(n) for the recursion stack, as the maximum depth of the recursion tree is n.

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
        // skip duplicate combinations
        if (i > start && candidates[i] == candidates[i-1]) continue;
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

int main() {
    vector<int> candidates = {10,1,2,7,6,1,5};
    int target = 8;
    vector<vector<int>> result = combinationSum2(candidates, target);
    for (auto& combination : result) {
        for (auto& num : combination) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [
  [1,1,6],
  [1,2,5],
  [1,7],
  [2,6]
]
```

## Key Takeaways
- Use recursion and backtracking to solve combination problems.
- Sort the input array to easily skip duplicate combinations.
- Use a helper function to perform the actual recursion and backtracking.