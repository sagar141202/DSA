# Combination Sum II

## Problem Statement
Given a collection of candidate numbers and a target number, find all unique combinations in the collection where the candidate numbers sum to the target. Each number in the collection may only be used once in the combination. The solution set must not contain duplicate combinations. For example, given candidate set [10,1,2,7,6,1,5] and target 8, one of the possible output is [1,1,6] (1+1+6 = 8, the numbers also can be [1,2,5], [1,7], [2,6]).

## Approach
The problem can be solved using recursion and backtracking, where we try to add each number in the candidate set to the current combination and recursively call the function with the remaining target. We also need to sort the candidate set and skip the duplicate numbers to avoid duplicate combinations. The base case is when the target becomes zero, which means we have found a valid combination.

## Complexity
- Time: O(2^n) where n is the number of candidates, because in the worst case, we might have to try all possible combinations.
- Space: O(n) for the recursion stack and storing the current combination.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& candidates, int start, int target, vector<int>& path, vector<vector<int>>& result) {
    if (target < 0) return; // if target is less than 0, it's not a valid combination
    if (target == 0) {
        result.push_back(path); // if target is 0, it's a valid combination
        return;
    }
    for (int i = start; i < candidates.size(); i++) {
        if (i > start && candidates[i] == candidates[i - 1]) continue; // skip duplicates
        path.push_back(candidates[i]);
        backtrack(candidates, i + 1, target - candidates[i], path, result);
        path.pop_back();
    }
}

vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    vector<vector<int>> result;
    vector<int> path;
    sort(candidates.begin(), candidates.end());
    backtrack(candidates, 0, target, path, result);
    return result;
}

int main() {
    vector<int> candidates = {10, 1, 2, 7, 6, 1, 5};
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
Output: 
[1,1,6]
[1,2,5]
[1,7]
[2,6]
```

## Key Takeaways
- Use recursion and backtracking to solve the problem.
- Sort the candidate set and skip duplicates to avoid duplicate combinations.
- Use a base case to stop the recursion when the target becomes zero.