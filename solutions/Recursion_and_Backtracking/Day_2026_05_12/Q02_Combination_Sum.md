# Combination Sum

## Problem Statement
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations in `candidates` where the candidate numbers sum to `target`. The same number may be used an unlimited number of times. The solution should be in ascending order and not contain duplicate combinations.

## Approach
The solution uses recursion and backtracking to find all combinations of numbers that sum to the target. It iterates over the candidates array, adding each number to the current combination and recursively calling the function with the updated target. If the target becomes zero, it means a valid combination has been found.

## Complexity
- Time: O(N^(T/M + 1)) where N is the number of candidates, T is the target, and M is the minimum value among the candidates
- Space: O(T/M) for the recursion stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& candidates, int target, int start, vector<int>& path, vector<vector<int>>& result) {
    if (target < 0) return; // base case: target becomes negative
    if (target == 0) {
        result.push_back(path); // found a valid combination
        return;
    }
    for (int i = start; i < candidates.size(); i++) {
        path.push_back(candidates[i]); // add current candidate to the path
        backtrack(candidates, target - candidates[i], i, path, result); // recursive call
        path.pop_back(); // backtrack: remove the last added candidate
    }
}

vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    vector<vector<int>> result;
    vector<int> path;
    backtrack(candidates, target, 0, path, result);
    return result;
}

int main() {
    vector<int> candidates = {2, 3, 5};
    int target = 8;
    vector<vector<int>> result = combinationSum(candidates, target);
    for (auto& combination : result) {
        for (auto& num : combination) {
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
Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
```

## Key Takeaways
- Use recursion and backtracking to solve problems that involve finding all combinations or permutations of a given set.
- The base case for the recursion should be well-defined to avoid infinite loops.
- Backtracking is essential to explore all possible branches of the solution space.