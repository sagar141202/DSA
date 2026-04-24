# Combination Sum II

## Problem Statement
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate number is greater than the previous one and the sum of the combination equals to target. Each number in candidates may only be used once in the combination. The solution set must not contain duplicate combinations. For example, given candidates = [10,1,2,7,6,1,5] and target = 8, the output should be [[1,1,6],[1,2,5],[1,7],[2,6]].

## Approach
The algorithm uses recursion and backtracking to generate all combinations. It sorts the candidates array first and then recursively tries to add each number to the current combination, skipping duplicates to ensure uniqueness.

## Complexity
- Time: O(2^n) where n is the number of candidates
- Space: O(n) for the recursion stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> current;
        sort(candidates.begin(), candidates.end());
        backtrack(result, current, candidates, target, 0);
        return result;
    }

    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& candidates, int target, int start) {
        if (target < 0) return;
        if (target == 0) {
            result.push_back(current);
            return;
        }
        for (int i = start; i < candidates.size(); i++) {
            if (i > start && candidates[i] == candidates[i - 1]) continue; // skip duplicates
            current.push_back(candidates[i]);
            backtrack(result, current, candidates, target - candidates[i], i + 1);
            current.pop_back();
        }
    }
};

```

## Test Cases
```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
Input: candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]
```

## Key Takeaways
- Sort the input array to simplify duplicate detection and ensure a consistent order for the combinations.
- Use a recursive backtracking approach to efficiently generate all combinations.
- Skip duplicate numbers in the recursive loop to ensure uniqueness of combinations.