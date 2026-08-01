# Combination Sum II

## Problem Statement
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate number is greater than the previous number and the sum of the numbers in the combination equals to the target. Each number in candidates may only be used once in the combination. The solution set must not contain duplicate combinations. For example, if the input is [10,1,2,7,6,1,5] and target is 8, then the output should be [[1,1,6],[1,2,5],[1,7],[2,6]].

## Approach
The problem can be solved using recursion and backtracking. We will sort the candidates array first and then use a helper function to find all combinations that sum up to the target. We will skip the duplicate numbers to ensure uniqueness of combinations.

## Complexity
- Time: O(2^n) where n is the number of candidates, because in the worst case, we might have to explore all possible combinations.
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
        // Skip duplicates to ensure uniqueness
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
- Use recursion and backtracking to solve combination problems.
- Sort the input array to handle duplicates efficiently.
- Use a helper function to perform the actual backtracking.