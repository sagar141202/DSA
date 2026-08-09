# Combination Sum

## Problem Statement
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations in `candidates` where the candidate numbers sum to `target`. The same number may be used an unlimited number of times. The solution should be in ascending order and should not contain duplicate combinations. For example, if the input is `candidates = [2,3,6,7]` and `target = 7`, the output should be `[[2,2,3],[7]]`.

## Approach
The algorithm uses recursion and backtracking to find all combinations that sum to the target. It iterates over the candidates array, adds each candidate to the current combination, and recursively calls the function with the updated target and combination.

## Complexity
- Time: O(N^(T/M + 1)) where N is the number of candidates, T is the target, and M is the minimum value in the candidates array
- Space: O(T/M) for the recursion stack

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
        comb.push_back(candidates[i]);
        backtrack(remain - candidates[i], comb, i, candidates, result);
        comb.pop_back();
    }
}

vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    vector<vector<int>> result;
    vector<int> comb;
    backtrack(target, comb, 0, candidates, result);
    return result;
}
```

## Test Cases
```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Input: candidates = [2], target = 1
Output: []
```

## Key Takeaways
- Use recursion and backtracking to solve problems that require finding all combinations or permutations.
- The key to this problem is to use a start index to avoid duplicate combinations.
- The time complexity is exponential in the worst case, but it can be improved by using a more efficient algorithm or data structure.