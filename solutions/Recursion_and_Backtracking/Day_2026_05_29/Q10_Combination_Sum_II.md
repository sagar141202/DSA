# Combination Sum II

## Problem Statement
Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`. Each number in `candidates` may only be used once in the combination. The solution set must not contain duplicate combinations. For example, if `candidates` is `[10,1,2,7,6,1,5]` and `target` is `8`, then the output will be `[ [1, 1, 6], [1, 2, 5], [1, 7], [2, 6] ]`. The input array `candidates` is not sorted, and the same number may be repeated.

## Approach
The problem can be solved using backtracking and recursion. The idea is to start with an empty combination and try to add each candidate number to it, ensuring that the sum does not exceed the target. We also need to avoid duplicate combinations.

## Complexity
- Time: O(2^n * n) where n is the number of candidates, due to the recursive nature of backtracking
- Space: O(n) for the recursion stack

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
        if (i > start && candidates[i] == candidates[i-1]) {
            continue;
        }
        comb.push_back(candidates[i]);
        backtrack(remain - candidates[i], comb, i + 1, candidates, result);
        comb.pop_back();
    }
}

vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    vector<vector<int>> result;
    vector<int> comb;
    sort(candidates.begin(), candidates.end()); // Sort to handle duplicates
    backtrack(target, comb, 0, candidates, result);
    return result;
}
```

## Test Cases
```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [ [1, 1, 6], [1, 2, 5], [1, 7], [2, 6] ]
```

## Key Takeaways
- Sort the input array to handle duplicate combinations efficiently
- Use backtracking to explore all possible combinations of candidate numbers
- Avoid duplicate combinations by skipping identical numbers in the sorted array