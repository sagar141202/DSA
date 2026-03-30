# Combination Sum II

## Problem Statement
Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`. Each number in `candidates` may only be used once in the combination. The solution should not contain duplicate combinations.

## Approach
The solution uses recursion and backtracking to generate all possible combinations of candidate numbers that sum to the target. It sorts the candidates array and skips duplicate numbers to ensure uniqueness.

## Complexity
- Time: O(2^n) where n is the number of candidates, as each candidate can either be included or excluded from the combination.
- Space: O(n) for the recursion stack, as the maximum depth of recursion is equal to the number of candidates.

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
        // Skip duplicates
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

int main() {
    vector<int> candidates = {10,1,2,7,6,1,5};
    int target = 8;
    vector<vector<int>> result = combinationSum2(candidates, target);
    for (auto& vec : result) {
        for (auto& num : vec) {
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
- The problem requires generating all unique combinations of candidate numbers that sum to the target, with each number used at most once.
- The solution uses recursion and backtracking to generate all possible combinations, and skips duplicate numbers to ensure uniqueness.
- The time complexity is exponential due to the recursive nature of the solution, while the space complexity is linear due to the recursion stack.