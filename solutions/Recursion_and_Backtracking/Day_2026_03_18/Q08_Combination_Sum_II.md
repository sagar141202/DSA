# Combination Sum II

## Problem Statement
Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`. Each number in `candidates` may only be used once in the combination. Note that the same number may be repeated in `candidates`, and in this case, the same combination should not be included more than once. The solution should not contain duplicate combinations.

## Approach
The problem can be solved using recursion and backtracking. We will sort the candidates array and then use a recursive function to find all combinations that sum up to the target. We will skip the duplicate combinations by checking if the current number is the same as the previous one.

## Complexity
- Time: O(2^n) where n is the number of candidates, because in the worst case, we have to try all possible combinations.
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
        // skip duplicates
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
- Use recursion and backtracking to find all combinations that sum up to the target.
- Sort the candidates array to skip duplicate combinations.
- Use a start index to ensure that each number is only used once in the combination.