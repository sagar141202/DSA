# Combination Sum

## Problem Statement
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations in candidates where the candidate number is a sum of target. The same number may be used an unlimited number of times. The solution set must not contain duplicate combinations. For example, if the input is candidates = [2,3,6,7] and target = 7, then the output should be [[2,2,3],[7]].

## Approach
The problem can be solved using recursion and backtracking. We start by iterating over the candidates array and for each candidate, we recursively call the function with the remaining target and the current combination. If the remaining target becomes zero, we add the current combination to the result. The algorithm ensures that duplicate combinations are not included in the result.

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

int main() {
    vector<int> candidates = {2, 3, 6, 7};
    int target = 7;
    vector<vector<int>> result = combinationSum(candidates, target);
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
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Input: candidates = [2], target = 1
Output: []
```

## Key Takeaways
- Use recursion and backtracking to solve problems that involve finding all combinations of a given set of elements.
- Use a helper function to perform the recursive calls and backtrack when necessary.
- Be careful with the base cases and the recursive calls to avoid duplicate combinations or incorrect results.