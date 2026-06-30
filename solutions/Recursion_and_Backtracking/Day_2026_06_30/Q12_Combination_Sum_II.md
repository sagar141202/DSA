# Combination Sum II

## Problem Statement
Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`. Each number in `candidates` may only be used once in the combination. Note that the same number may be repeated in `candidates`, and in this case, the same combination should not be included more than once. The solution should return a list of all unique combinations that sum up to the target.

## Approach
The solution uses recursion and backtracking to explore all possible combinations of candidate numbers. It sorts the candidates array to handle duplicates efficiently and ensures that each number is only used once in each combination.

## Complexity
- Time: O(2^n) where n is the number of candidates, due to the recursive nature of the solution.
- Space: O(n) for the recursion stack in the worst case.

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
        for (int num : vec) {
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
- Sorting the candidates array helps in efficiently handling duplicates.
- Using a `start` index in the recursive function ensures that each candidate number is used only once in each combination.
- Backtracking is essential for exploring all possible combinations without exceeding the target sum.