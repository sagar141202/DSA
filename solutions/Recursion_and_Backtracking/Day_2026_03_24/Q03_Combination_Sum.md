# Combination Sum

## Problem Statement
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations in `candidates` where the candidate numbers sum to `target`. The same number may be used an unlimited number of times. The solution should be presented in a non-decreasing order.

## Approach
The problem can be solved using recursion and backtracking. We will iterate through each candidate number and recursively try to find combinations that sum up to the remaining target. If the remaining target becomes zero, we have found a valid combination.

## Complexity
- Time: O(N^(T/M + 1)) where N is the number of candidates, T is the target, and M is the minimum value among the candidates
- Space: O(T/M) for the recursion stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(int remain, vector<int>& comb, int start, vector<int>& candidates, vector<vector<int>>& result) {
    // Base case: when the remaining value becomes zero, it means we have found a valid combination
    if (remain == 0) {
        result.push_back(comb);
        return;
    }
    // Iterate through each candidate number
    for (int i = start; i < candidates.size(); i++) {
        // If the current candidate number is greater than the remaining value, we can break the loop
        if (candidates[i] > remain) break;
        // Add the current candidate number to the current combination
        comb.push_back(candidates[i]);
        // Recursively try to find combinations that sum up to the remaining target
        backtrack(remain - candidates[i], comb, i, candidates, result);
        // Remove the last added candidate number from the current combination for backtracking
        comb.pop_back();
    }
}

vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    vector<vector<int>> result;
    vector<int> comb;
    // Sort the candidates in non-decreasing order
    sort(candidates.begin(), candidates.end());
    backtrack(target, comb, 0, candidates, result);
    return result;
}

int main() {
    vector<int> candidates = {2, 3, 5};
    int target = 8;
    vector<vector<int>> result = combinationSum(candidates, target);
    for (auto& comb : result) {
        for (int num : comb) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: candidates = [2, 3, 5], target = 8
Output: 
[2, 2, 2, 2]
[2, 3, 3]
[3, 5]
```

## Key Takeaways
- Use recursion and backtracking to find all unique combinations that sum up to the target.
- Sort the candidate numbers in non-decreasing order to handle duplicate combinations and improve efficiency.
- Use a base case to handle the situation when the remaining target becomes zero, indicating a valid combination has been found.