# Combination Sum II

## Problem Statement
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate number is less than or equal to the target. Each number in candidates may only be used once in the combination. Return a list of all possible combinations. The same combination should not be counted more than once. The combination should be sorted in ascending order.

## Approach
The problem can be solved using recursion and backtracking. We will iterate over the candidates array and for each candidate, we will recursively call the function with the remaining target and the next index. If the target becomes zero, it means we have found a valid combination.

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

int main() {
    vector<int> candidates = {10,1,2,7,6,1,5};
    int target = 8;
    vector<vector<int>> result = combinationSum2(candidates, target);
    for (auto& vec : result) {
        for (auto& num : vec) {
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
- Use recursion and backtracking to solve the problem.
- Sort the candidates array to ensure that the combinations are in ascending order.
- Skip duplicates to ensure uniqueness of combinations.