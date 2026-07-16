# Combination Sum II

## Problem Statement
Given a collection of candidate numbers and a target number, find all unique combinations in the collection where the candidate numbers sum to the target. Each number in the collection may only be used once in the combination. The solution should not contain duplicate combinations. For example, given candidate set [10,1,2,7,6,1,5] and target 8, a solution set is: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]].

## Approach
The problem can be solved using recursion and backtracking. We will iterate through the candidate numbers and recursively try to find combinations that sum to the target. We will also skip duplicate numbers to avoid duplicate combinations. The base case for the recursion will be when the target becomes zero, at which point we have found a valid combination.

## Complexity
- Time: O(2^n) where n is the number of candidate numbers, as in the worst case we might have to try all possible combinations.
- Space: O(n) for the recursion stack, as the maximum depth of the recursion tree can be n.

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
        // Skip duplicates
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
Output: [[1,1,6], [1,2,5], [1,7], [2,6]]
```

## Key Takeaways
- Use recursion and backtracking to try all possible combinations of candidate numbers.
- Skip duplicate numbers to avoid duplicate combinations.
- Use a base case to stop the recursion when the target becomes zero, indicating a valid combination has been found.