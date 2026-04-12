# Combination Sum

## Problem Statement
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations in `candidates` where the candidate numbers sum to `target`. The same number may be used an unlimited number of times. The solution should be in non-decreasing order.

## Approach
The algorithm uses recursion and backtracking to find all combinations that sum up to the target. It starts with an empty combination and explores all possible additions of numbers from the candidates array. The base case is when the sum of the current combination equals the target.

## Complexity
- Time: O(N^(T/M + 1)) where N is the number of candidates, T is the target, and M is the minimum value among the candidates.
- Space: O(T/M) for the recursion stack.

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
            if (remaining >= candidates[i]) {
                current.push_back(candidates[i]);
                backtrack(result, current, candidates, remaining - candidates[i], i);
                current.pop_back();
            }
        }
    }
};

int main() {
    Solution solution;
    vector<int> candidates = {2, 3, 6, 7};
    int target = 7;
    vector<vector<int>> result = solution.combinationSum(candidates, target);
    for (auto combination : result) {
        for (auto num : combination) {
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
```

## Key Takeaways
- Use recursion and backtracking to explore all possible combinations.
- The base case is when the sum of the current combination equals the target.
- Use a helper function to perform the backtracking and add combinations to the result when the base case is reached.