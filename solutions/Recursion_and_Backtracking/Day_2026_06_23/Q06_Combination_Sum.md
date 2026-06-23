# Combination Sum

## Problem Statement
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations in `candidates` where the candidate numbers sum to `target`. The same number may be used an unlimited number of times. The solution should be in non-decreasing order and each combination should not contain duplicate triplets.

## Approach
The problem can be solved using recursion and backtracking, by iterating over the candidates array and recursively calling the function with the remaining target and the current combination. The base case is when the target becomes zero, at which point the current combination is added to the result.

## Complexity
- Time: O(N^(T/M + 1)) where N is the number of candidates, T is the target, and M is the minimum value in the candidates array
- Space: O(T/M) for the recursion stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(int remain, vector<int>& comb, int start, vector<int>& candidates, vector<vector<int>>& result) {
    // Base case: when the target becomes zero, add the current combination to the result
    if (remain == 0) {
        result.push_back(comb);
        return;
    }
    // Iterate over the candidates array
    for (int i = start; i < candidates.size(); i++) {
        // If the current candidate is greater than the remaining target, break the loop
        if (candidates[i] > remain) break;
        // Add the current candidate to the current combination
        comb.push_back(candidates[i]);
        // Recursively call the function with the remaining target and the updated combination
        backtrack(remain - candidates[i], comb, i, candidates, result);
        // Remove the last added candidate from the current combination (backtracking)
        comb.pop_back();
    }
}

vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    vector<vector<int>> result;
    vector<int> comb;
    // Sort the candidates array in ascending order
    sort(candidates.begin(), candidates.end());
    backtrack(target, comb, 0, candidates, result);
    return result;
}

int main() {
    vector<int> candidates = {2, 3, 5};
    int target = 8;
    vector<vector<int>> result = combinationSum(candidates, target);
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
Input: candidates = [2, 3, 5], target = 8
Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
```

## Key Takeaways
- Use recursion and backtracking to solve problems that require exploring all possible combinations of a given set of elements.
- The base case is crucial in recursion, and it should be well-defined to avoid infinite recursion.
- Backtracking is used to restore the state of the system after exploring a particular branch, which helps in exploring other branches.