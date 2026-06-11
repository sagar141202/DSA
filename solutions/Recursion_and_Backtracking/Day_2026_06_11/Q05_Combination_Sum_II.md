# Combination Sum II

## Problem Statement
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate number is greater than the previous number and the sum of the numbers in the combination is equal to the target. Each number in candidates may only be used once in the combination. The solution set must not contain duplicate combinations.

## Approach
We will use a recursive backtracking approach to solve this problem, starting with an empty combination and adding numbers one by one. We will sort the candidates array to ensure that we can skip duplicates and only consider combinations where each number is greater than the previous one.

## Complexity
- Time: O(2^n) where n is the number of candidates, as in the worst case we might have to try all possible combinations.
- Space: O(n) for the recursion stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& candidates, int target, int start, vector<int>& path, vector<vector<int>>& result) {
    if (target < 0) return; // base case: if target becomes negative, stop exploring this path
    if (target == 0) {
        result.push_back(path); // if target becomes zero, we have found a valid combination
        return;
    }
    for (int i = start; i < candidates.size(); i++) {
        if (i > start && candidates[i] == candidates[i-1]) continue; // skip duplicates
        path.push_back(candidates[i]); // add the current number to the current path
        backtrack(candidates, target - candidates[i], i + 1, path, result); // recursively explore the next numbers
        path.pop_back(); // remove the current number from the current path (backtracking)
    }
}

vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    vector<vector<int>> result;
    vector<int> path;
    sort(candidates.begin(), candidates.end()); // sort the candidates array
    backtrack(candidates, target, 0, path, result);
    return result;
}
```

## Test Cases
```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
```

## Key Takeaways
- Use recursive backtracking to explore all possible combinations of numbers.
- Sort the candidates array to ensure that each number is greater than the previous one and to skip duplicates.
- Use a base case to stop exploring a path when the target becomes negative, and add a combination to the result when the target becomes zero.