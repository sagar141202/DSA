# Permutations

## Problem Statement
Given a collection of distinct numbers, return all possible permutations. For example, if the input is [1, 2, 3], a solution set is [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]. The input will not contain duplicates and will contain at least one element.

## Approach
The problem can be solved using recursion and backtracking, where we generate all permutations by swapping each element with the remaining elements. We start with an empty permutation and add elements one by one, backtracking when a permutation is complete.

## Complexity
- Time: O(N!)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        backtrack(result, nums, 0);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& nums, int start) {
        if (start == nums.size()) {
            result.push_back(nums);
        } else {
            for (int i = start; i < nums.size(); i++) {
                swap(nums[start], nums[i]);
                backtrack(result, nums, start + 1);
                swap(nums[start], nums[i]);
            }
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
- Recursion and backtracking can be used to generate all permutations of a given set.
- The time complexity of generating all permutations is O(N!), where N is the number of elements in the set.
- The space complexity of generating all permutations is O(N), where N is the number of elements in the set.