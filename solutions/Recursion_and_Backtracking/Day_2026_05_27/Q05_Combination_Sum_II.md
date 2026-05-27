# Combination Sum II

## Problem Statement
Given a collection of candidate numbers and a target number, find all unique combinations in the candidates where the candidate numbers sum to the target. Each number in the candidates may only be used once in the combination. The solution set must not contain duplicate combinations. For example, if the input is `candidates = [10,1,2,7,6,1,5]` and `target = 8`, then the output should be `[ [1, 1, 6], [1, 2, 5], [1, 7], [2, 6] ]`. The input array may contain duplicate numbers, and the numbers may be negative or positive.

## Approach
The solution involves using recursion and backtracking to generate all possible combinations of the candidate numbers. We will sort the candidates array and use a helper function to recursively find combinations that sum to the target. The base case for the recursion is when the target becomes zero, at which point we have found a valid combination.

## Complexity
- Time: O(2^n) due to the recursive nature of the solution, where n is the number of candidates
- Space: O(n) for the recursion stack and storing the result

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(int remain, vector<int>& comb, int start, vector<int>& candidates, vector<vector<int>>& result) {
    if (remain == 0) {
        result.push_back(comb);
        return;
    } else if (remain < 0) {
        return;
    }
    for (int i = start; i < candidates.size(); i++) {
        // Skip duplicates to ensure unique combinations
        if (i > start && candidates[i] == candidates[i-1]) continue;
        comb.push_back(candidates[i]);
        backtrack(remain - candidates[i], comb, i + 1, candidates, result);
        comb.pop_back();
    }
}

vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    vector<vector<int>> result;
    vector<int> comb;
    sort(candidates.begin(), candidates.end());
    backtrack(target, comb, 0, candidates, result);
    return result;
}

int main() {
    vector<int> candidates = {10,1,2,7,6,1,5};
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
Output: [ [1, 1, 6], [1, 2, 5], [1, 7], [2, 6] ]
```

## Key Takeaways
- Use recursion and backtracking to solve problems that involve generating combinations or permutations.
- Sort the input array to handle duplicate values and ensure unique combinations.
- Use a helper function to perform the recursive operations and keep track of the current combination and remaining target.