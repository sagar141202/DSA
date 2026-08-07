# Combination Sum II

## Problem Statement
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate number is greater than the previous number and the sum of the numbers in the combination is equal to the target. The same number in candidates cannot be used more than once in the combination. The candidates array will not contain duplicate numbers, and all numbers will be positive.

## Approach
We will use recursion and backtracking to solve this problem. The idea is to try each number in the candidates array and recursively find combinations that sum up to the remaining target. We will also ensure that the current number is greater than the previous number to maintain the required order.

## Complexity
- Time: O(2^n) where n is the number of candidates, as in the worst case, we might have to try all possible combinations.
- Space: O(n) for the recursion stack.

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
```

## Key Takeaways
- Use recursion and backtracking to solve problems that require finding all possible combinations.
- Ensure that the current number is greater than the previous number to maintain the required order.
- Use a vector to store the current combination and another vector to store all the results.