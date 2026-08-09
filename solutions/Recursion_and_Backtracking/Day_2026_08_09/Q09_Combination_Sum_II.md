# Combination Sum II

## Problem Statement
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate number is greater than the previous number in the combination, and the sum of the combination is equal to the target. The same number may not be used more than once in the combination. The solution set must not contain duplicate combinations. For example, if the input is [10,1,2,7,6,1,5] and the target is 8, the output should be [[1,1,6],[1,2,5],[1,7],[2,6]].

## Approach
We will use recursion and backtracking to solve this problem. The idea is to start with an empty combination and add numbers to it one by one, making sure that the sum does not exceed the target and that each number is greater than the previous one. If the sum equals the target, we add the combination to the result.

## Complexity
- Time: O(2^n) where n is the number of candidates, because in the worst case, we might have to generate all possible combinations.
- Space: O(n) for the recursion stack.

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
- Use recursion and backtracking to generate all combinations.
- Sort the candidates array to easily skip duplicates and ensure that each number is greater than the previous one.
- Use a helper function (backtrack) to perform the recursion and backtracking.