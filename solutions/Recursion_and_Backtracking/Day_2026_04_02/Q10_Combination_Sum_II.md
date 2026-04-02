# Combination Sum II

## Problem Statement
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate number is greater than the previous number and the sum of the numbers in the combination equals to the target. The same number may not be used unlimited times, but each number can be used only as many times as it appears in the candidates. Return a list of all unique combinations.

## Approach
The problem can be solved using recursion and backtracking, by iterating over the candidates and adding them to the current combination if the sum does not exceed the target. The algorithm ensures that each number is used only as many times as it appears in the candidates and that the combinations are unique.

## Complexity
- Time: O(2^n) where n is the number of candidates, in the worst case when all candidates can be added to the combination
- Space: O(n) for the recursive call stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& candidates, int start, int target, vector<int>& current, vector<vector<int>>& result) {
    if (target < 0) return; // base case: sum exceeds target
    if (target == 0) {
        result.push_back(current); // found a valid combination
        return;
    }
    for (int i = start; i < candidates.size(); i++) {
        if (i > start && candidates[i] == candidates[i-1]) continue; // skip duplicates
        current.push_back(candidates[i]); // add current candidate to the combination
        backtrack(candidates, i + 1, target - candidates[i], current, result); // recursive call
        current.pop_back(); // backtrack
    }
}

vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    sort(candidates.begin(), candidates.end()); // sort candidates to handle duplicates
    vector<vector<int>> result;
    vector<int> current;
    backtrack(candidates, 0, target, current, result);
    return result;
}
```

## Test Cases
```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible combinations
- Sort the candidates to handle duplicates and ensure that each combination is unique
- Use a base case to stop the recursion when the sum exceeds the target or when a valid combination is found