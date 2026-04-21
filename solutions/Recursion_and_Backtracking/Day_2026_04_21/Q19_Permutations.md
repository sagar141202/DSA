# Permutations

## Problem Statement
Given a collection of distinct numbers, return all possible permutations. For example, if the input is [1, 2, 3], a solution set is [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]. The input array will not contain duplicates, and the length of the array will be between 1 and 6.

## Approach
The solution uses backtracking to generate all permutations of the input array. It starts by selecting the first element, then recursively generates all permutations of the remaining elements. The base case is when the input array is empty, at which point the function returns. The algorithm swaps each element with the current element to generate all permutations.

## Complexity
- Time: O(n!)
- Space: O(n)

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
        }
        for (int i = start; i < nums.size(); i++) {
            swap(nums[start], nums[i]);
            backtrack(result, nums, start + 1);
            swap(nums[start], nums[i]);
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
- Use backtracking to generate all permutations of an array by swapping elements and recursively generating permutations of the remaining elements.
- The base case is when the input array is empty, at which point the function returns.
- The time complexity is O(n!) because there are n! permutations of an array of length n.