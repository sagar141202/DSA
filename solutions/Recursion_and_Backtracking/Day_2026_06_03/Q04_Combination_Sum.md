# Combination Sum

## Problem Statement
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations in `candidates` where the candidate numbers sum to `target`. The same number may be used an unlimited number of times. The solution should be found using recursion and backtracking.

## Approach
The problem can be solved by using a recursive approach with backtracking to find all combinations of numbers that sum up to the target. We will use a helper function to recursively explore all possible combinations.

## Complexity
- Time: O(N^(T/M + 1)) where N is the number of candidates, T is the target, and M is the minimum value among candidates
- Space: O(T/M) for recursion stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(int remain, vector<int>& comb, int start, vector<int>& candidates, vector<vector<int>>& result) {
    // base case: when remaining value is 0, it means we have found a valid combination
    if (remain == 0) {
        result.push_back(comb);
        return;
    }
    // iterate over the candidates array
    for (int i = start; i < candidates.size(); i++) {
        // if current candidate is greater than remaining value, break the loop
        if (candidates[i] > remain) break;
        // add current candidate to current combination
        comb.push_back(candidates[i]);
        // recursively call backtrack function with updated remaining value and current combination
        backtrack(remain - candidates[i], comb, i, candidates, result);
        // remove last added candidate from current combination (backtracking)
        comb.pop_back();
    }
}

vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    vector<vector<int>> result;
    vector<int> comb;
    // sort the candidates array to optimize the backtracking process
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
- Use recursion and backtracking to explore all possible combinations of numbers.
- Sort the candidates array to optimize the backtracking process by breaking the loop when the current candidate is greater than the remaining value.
- Use a helper function to recursively call itself with updated parameters.