# Combination Sum II

## Problem Statement
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate number is greater than the previous number in the combination, and the sum of the combination equals to target. The same number may be used an unlimited number of times in the combination. The solution set must not contain duplicate combinations.

## Approach
We will use recursion and backtracking to solve this problem. The idea is to try each number in the candidates array and recursively find combinations that sum up to the remaining target. We will also sort the candidates array to ensure that the combinations are unique.

## Complexity
- Time: O(2^n) where n is the length of the candidates array
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
        // Skip duplicates
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
- The backtracking approach is useful for solving problems that require exploring all possible combinations.
- Sorting the input array can help to avoid duplicate combinations.
- Using a recursion stack can help to simplify the code and improve readability.