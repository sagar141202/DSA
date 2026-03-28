# Combination Sum

## Problem Statement
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations in `candidates` where the candidate numbers sum to `target`. The same number may be used an unlimited number of times. Each combination should be sorted in ascending order. The solution should be able to handle large inputs.

## Approach
The solution uses recursion and backtracking to generate all combinations of numbers that sum to the target. It iterates over the candidates array, adding each number to the current combination and recursively calling the function with the updated target. If the target becomes zero, it means a valid combination has been found.

## Complexity
- Time: O(N^(T/M + 1)) where N is the number of candidates, T is the target, and M is the minimum value among the candidates
- Space: O(T/M) for the recursion stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(int remain, vector<int>& comb, int start, vector<int>& candidates, vector<vector<int>>& result) {
    // base case: if the remaining value is zero, it means we have found a valid combination
    if (remain == 0) {
        result.push_back(comb);
        return;
    }
    // iterate over the candidates array starting from the start index
    for (int i = start; i < candidates.size(); i++) {
        // if the current candidate is greater than the remaining value, break the loop
        if (candidates[i] > remain) break;
        // add the current candidate to the current combination
        comb.push_back(candidates[i]);
        // recursively call the backtrack function with the updated remaining value and combination
        backtrack(remain - candidates[i], comb, i, candidates, result);
        // remove the last added candidate from the combination (backtracking)
        comb.pop_back();
    }
}

vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    vector<vector<int>> result;
    vector<int> comb;
    // sort the candidates array in ascending order
    sort(candidates.begin(), candidates.end());
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
- Use recursion and backtracking to generate all combinations of numbers that sum to the target.
- Sort the candidates array in ascending order to prune branches that will exceed the target.
- Use a start index to allow the same number to be used an unlimited number of times in the combination.