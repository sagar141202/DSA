# Combination Sum II

## Problem Statement
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate number is greater than the previous number and the sum of the candidate numbers is equal to the target. The same number may not be used more than once in a combination. The solution set must not contain duplicate combinations.

## Approach
The problem can be solved using recursion and backtracking, where we try to add each candidate number to the current combination and recursively call the function with the updated target and combination. We also need to sort the candidates and skip duplicates to ensure unique combinations.

## Complexity
- Time: O(2^n) where n is the number of candidates
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

int main() {
    vector<int> candidates = {10,1,2,7,6,1,5};
    int target = 8;
    vector<vector<int>> result = combinationSum2(candidates, target);
    for (auto& comb : result) {
        for (auto& num : comb) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
```

## Key Takeaways
- Use recursion and backtracking to solve combination problems
- Sort the input array to ensure unique combinations
- Skip duplicates to avoid duplicate combinations in the result set