# Combination Sum

## Problem Statement
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations in `candidates` where the candidate numbers sum to `target`. The same number may be used an unlimited number of times. The solution should be in non-decreasing order and each combination should not be repeated.

## Approach
This problem can be solved using recursion and backtracking. We start by selecting each number in the array and then recursively finding combinations that sum up to the remaining target. We use backtracking to explore all possible combinations.

## Complexity
- Time: O(N^(T/M + 1)) where N is the number of candidates, T is the target, and M is the minimum value among the candidates
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

    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& candidates, int remain, int start) {
        if (remain == 0) {
            result.push_back(current);
            return;
        }
        for (int i = start; i < candidates.size(); i++) {
            if (candidates[i] <= remain) {
                current.push_back(candidates[i]);
                backtrack(result, current, candidates, remain - candidates[i], i);
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
- Use recursion and backtracking to explore all possible combinations.
- Use a helper function to perform the backtracking.
- Use a vector to store the current combination and update it during the backtracking process.