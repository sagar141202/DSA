# Combination Sum

## Problem Statement
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations in `candidates` where the candidate numbers sum to `target`. The same number may be used an unlimited number of times. The solution should be in non-decreasing order.

## Approach
The problem can be solved using recursion and backtracking, where we try to add each number in the candidates array to the current combination and recursively call the function with the remaining sum. If the remaining sum becomes zero, we have found a valid combination.

## Complexity
- Time: O(N^(T/M + 1)) where N is the number of candidates, T is the target sum, and M is the minimum value among the candidates
- Space: O(T/M) for the recursion stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> current;
        backtrack(result, current, candidates, target, 0);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& candidates, int remaining, int start) {
        if (remaining == 0) {
            result.push_back(current);
            return;
        }
        for (int i = start; i < candidates.size(); i++) {
            if (candidates[i] <= remaining) {
                current.push_back(candidates[i]);
                backtrack(result, current, candidates, remaining - candidates[i], i);
                current.pop_back();
            }
        }
    }
};

int main() {
    Solution solution;
    vector<int> candidates = {2, 3, 5};
    int target = 8;
    vector<vector<int>> result = solution.combinationSum(candidates, target);
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
- Use recursion and backtracking to solve problems that involve trying different combinations of elements.
- Keep track of the current combination and the remaining sum to avoid duplicates and ensure that the solution is in non-decreasing order.
- Use a base case to stop the recursion when the remaining sum becomes zero, indicating that a valid combination has been found.