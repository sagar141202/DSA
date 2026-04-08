# Combination Sum

## Problem Statement
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations in `candidates` where the candidate numbers sum to `target`. The same number may be used an unlimited number of times. The solution should be in non-decreasing order.

## Approach
The problem can be solved using recursion and backtracking, where we try adding each number to the current combination and recursively call the function with the updated target. If the target becomes zero, we have found a valid combination.

## Complexity
- Time: O(N^(T/M + 1)) where N is the number of candidates, T is the target, and M is the minimum value among the candidates
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
    vector<int> candidates = {2, 3, 5};
    int target = 8;
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
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Input: candidates = [2], target = 1
Output: []
Input: candidates = [1], target = 2
Output: [[1,1]]
```

## Key Takeaways
- Use recursion and backtracking to try all possible combinations of numbers
- Use a helper function `backtrack` to simplify the code and avoid repeated calculations
- Use a vector `comb` to store the current combination of numbers and a vector `result` to store all valid combinations.