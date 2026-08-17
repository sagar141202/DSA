# Combination Sum II

## Problem Statement
Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`. Each number in `candidates` may only be used once in the combination. The solution should not contain duplicate combinations.

## Approach
The approach involves using recursion and backtracking to explore all possible combinations of candidate numbers. We sort the candidates array to efficiently skip duplicate combinations. The algorithm recursively selects numbers from the candidates array, ensuring that each number is used only once.

## Complexity
- Time: O(2^n) where n is the number of candidates, due to the recursive nature of the algorithm
- Space: O(n) for the recursion stack in the worst case

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
- Use recursion and backtracking to explore all possible combinations of candidate numbers.
- Sort the candidates array to efficiently skip duplicate combinations.
- Ensure each number in the candidates array is used only once in the combination by passing `i + 1` to the recursive call.