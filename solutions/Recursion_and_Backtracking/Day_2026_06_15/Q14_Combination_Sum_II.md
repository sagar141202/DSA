# Combination Sum II

## Problem Statement
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate number is greater than the previous one and the sum of the numbers in the combination is equal to the target. The same number may not be used more than once in the combination. The solution should return a list of all unique combinations. For example, given candidates = [10,1,2,7,6,1,5] and target = 8, the output should be [[1,1,6],[1,2,5],[1,7],[2,6]].

## Approach
The problem can be solved using recursion and backtracking, where we try to add each number to the current combination and recursively call the function with the updated combination and target. If the target becomes zero, it means we have found a valid combination.

## Complexity
- Time: O(2^n) where n is the number of candidates, because in the worst case, we might have to try all possible combinations.
- Space: O(n) for the recursion stack and the space used to store the current combination.

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
        if (i > start && candidates[i] == candidates[i-1]) {
            continue;
        }
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
        for (auto& num : vec) {
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
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
Input: candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]
```

## Key Takeaways
- Use recursion and backtracking to solve problems that require exploring all possible combinations.
- Sort the input array to handle duplicates and ensure unique combinations.
- Use a start index to avoid using the same number more than once in the combination.