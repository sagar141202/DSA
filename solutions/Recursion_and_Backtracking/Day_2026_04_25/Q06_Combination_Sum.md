# Combination Sum

## Problem Statement
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations in `candidates` where the candidate numbers sum to `target`. The same number may be used an unlimited number of times. The solution should be in lexicographic order.

## Approach
The problem can be solved using recursion and backtracking, where we try to add each number to the current combination and recursively find the remaining sum. We use a helper function to perform the recursion and backtracking. The base case is when the remaining sum is 0, in which case we add the current combination to the result.

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
        sort(candidates.begin(), candidates.end());
        backtrack(result, current, candidates, target, 0);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& candidates, int remaining, int start) {
        if (remaining == 0) {
            result.push_back(current);
            return;
        }
        for (int i = start; i < candidates.size(); i++) {
            if (candidates[i] > remaining) break;
            current.push_back(candidates[i]);
            backtrack(result, current, candidates, remaining - candidates[i], i);
            current.pop_back();
        }
    }
};

```

## Test Cases
```
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

## Key Takeaways
- Use recursion and backtracking to try all possible combinations of numbers.
- Use a helper function to perform the recursion and backtracking.
- Sort the candidates array to ensure the result is in lexicographic order.