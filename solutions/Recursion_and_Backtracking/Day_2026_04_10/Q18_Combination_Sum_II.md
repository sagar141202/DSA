# Combination Sum II

## Problem Statement
Given a collection of candidate numbers and a target number, find all unique combinations in the candidate numbers where the candidate number is greater than the previous number in the combination, and the sum of the combination is equal to the target number. The same number may not be used more than once in the combination. The candidate numbers are non-negative and are sorted in ascending order. For example, if the input is [10,1,2,7,6,1,5] and the target is 8, the output should be [[1,1,6],[1,2,5],[1,7],[2,6]].

## Approach
The problem can be solved using recursion and backtracking. We start by iterating over the candidate numbers and for each number, we recursively find all combinations that sum up to the remaining target. We use backtracking to explore all possible combinations.

## Complexity
- Time: O(2^n) where n is the number of candidate numbers
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
Input: [10,1,2,7,6,1,5], 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
Input: [2,5,2,1,2], 5
Output: [[1,2,2],[5]]
```

## Key Takeaways
- Use recursion and backtracking to explore all possible combinations.
- Skip duplicates to ensure unique combinations.
- Sort the candidate numbers to simplify the backtracking process.