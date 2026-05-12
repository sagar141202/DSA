# Combination Sum II

## Problem Statement
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate number is greater than the previous number in the combination, and the sum of the combination is equal to the target. Each number in candidates may only be used once in the combination. The same number may not be used more than once in a combination. The problem constraints are: 1 <= candidates.length <= 50, 1 <= candidates[i] <= 200, and all elements of candidates are distinct. The target is in the range [1, 500].

## Approach
The problem is solved using recursion and backtracking, where we try to add each candidate to the current combination and recursively call the function with the updated combination and remaining sum. If the sum exceeds the target, we backtrack and try the next candidate. The key is to sort the candidates first and skip duplicates to avoid duplicate combinations.

## Complexity
- Time: O(2^n) where n is the number of candidates, as in the worst case, we might have to try all possible combinations.
- Space: O(n) for the recursion stack and storing the current combination.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        // Sort the candidates to handle duplicates and start from the smallest number
        sort(candidates.begin(), candidates.end());
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
            // Skip duplicates to avoid duplicate combinations
            if (i > start && candidates[i] == candidates[i-1]) continue;
            // If the current candidate exceeds the remaining sum, we can break the loop
            if (candidates[i] > remaining) break;
            current.push_back(candidates[i]);
            backtrack(result, current, candidates, remaining - candidates[i], i + 1);
            current.pop_back();
        }
    }
};

```

## Test Cases
```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
```

## Key Takeaways
- Sort the candidates to efficiently skip duplicates and break the loop when the current candidate exceeds the remaining sum.
- Use a recursive function to try all possible combinations and backtrack when the sum exceeds the target.
- Skip duplicates by checking if the current candidate is the same as the previous one and if the current index is greater than the start index.