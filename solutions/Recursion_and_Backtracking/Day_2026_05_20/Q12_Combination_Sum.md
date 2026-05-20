# Combination Sum

## Problem Statement
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations in `candidates` where the candidate numbers sum to `target`. The same number may be used an unlimited number of times. The solution should be able to handle large inputs and should be efficient in terms of time and space complexity. For example, if `candidates = [2,3,6,7]` and `target = 7`, then the output should be `[[2,2,3],[7]]`. The input array is not sorted, and the numbers can be negative, zero, or positive.

## Approach
The problem can be solved using recursion and backtracking. We start by iterating over each number in the candidates array and recursively call the function with the remaining target and the current combination. We use backtracking to explore all possible combinations.

## Complexity
- Time: O(N^(T/M + 1)) where N is the number of candidates, T is the target, and M is the minimum value in the candidates array
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

    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& candidates, int target, int start) {
        if (target < 0) return; // base case: target is less than 0
        if (target == 0) {
            result.push_back(current); // add current combination to result
            return;
        }
        for (int i = start; i < candidates.size(); i++) {
            current.push_back(candidates[i]); // add current number to current combination
            backtrack(result, current, candidates, target - candidates[i], i); // recursive call
            current.pop_back(); // remove current number from current combination (backtracking)
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
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Input: candidates = [2], target = 1
Output: []
```

## Key Takeaways
- Use recursion and backtracking to solve the problem efficiently.
- Handle the base cases carefully, such as when the target is less than 0 or equal to 0.
- Use a helper function to perform the recursive calls and backtracking.