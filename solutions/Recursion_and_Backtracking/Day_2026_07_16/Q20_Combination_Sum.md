# Combination Sum

## Problem Statement
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations in `candidates` where the candidate numbers sum to `target`. The same number may be used an unlimited number of times. The solution should be in a non-decreasing order.

## Approach
The problem can be solved using recursion and backtracking. The idea is to try each number in the candidates array and recursively find the combinations that sum to the remaining target. If the remaining target becomes zero, it means we have found a valid combination.

## Complexity
- Time: O(N^(T/M + 1)) where N is the number of candidates, T is the target sum, and M is the minimum value among the candidates
- Space: O(T/M) for the recursion stack

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
        comb.push_back(candidates[i]);
        backtrack(remain - candidates[i], comb, i, candidates, result);
        comb.pop_back();
    }
}

vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    vector<vector<int>> result;
    vector<int> comb;
    backtrack(target, comb, 0, candidates, result);
    return result;
}

int main() {
    vector<int> candidates = {2, 3, 5};
    int target = 8;
    vector<vector<int>> result = combinationSum(candidates, target);
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
Input: candidates = [2, 3, 5], target = 8
Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
```

## Key Takeaways
- Use recursion and backtracking to solve problems that involve finding all possible combinations.
- Make sure to handle the base cases correctly, such as when the remaining target becomes zero or negative.
- Use a helper function to perform the backtracking, and pass the necessary parameters to it.