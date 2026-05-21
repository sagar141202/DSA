# Permutations

## Problem Statement
Given a collection of distinct numbers, return all possible permutations. For example, if the input is [1, 2, 3], a solution set is [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]. The input will not contain duplicate numbers and will be in the range of 1 to 9.

## Approach
The algorithm uses recursion and backtracking to generate all permutations of the input array. It iterates over each element, adds it to the current permutation, and recursively generates permutations for the remaining elements. After each recursive call, it backtracks by removing the last added element.

## Complexity
- Time: O(n * n!)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        backtrack(result, current, nums);
        return result;
    }

    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& nums) {
        if (current.size() == nums.size()) {
            result.push_back(current);
            return;
        }
        for (int i = 0; i < nums.size(); i++) {
            if (find(current.begin(), current.end(), nums[i]) != current.end()) {
                continue;
            }
            current.push_back(nums[i]);
            backtrack(result, current, nums);
            current.pop_back();
        }
    }
};
```

## Test Cases
```
Input: [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

## Key Takeaways
- Use recursion and backtracking to generate all permutations of an array.
- Ensure that each element is added to the current permutation only once to avoid duplicates.
- Backtrack after each recursive call to explore other possible permutations.