# Permutations
## Problem Statement
Given a collection of distinct numbers, return all possible permutations. For example, if the input is [1, 2, 3], a solution set is [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]. The input array will not contain duplicates and 1 <= nums.length <= 6.

## Approach
The problem can be solved using backtracking, a form of recursion. We start by selecting each number in the array as the first number in the permutation, then recursively generate all permutations of the remaining numbers. We use a helper function to perform the backtracking.

## Complexity
- Time: O(N!), where N is the length of the input array, because there are N! permutations.
- Space: O(N), for the recursion stack.

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
            // Swap the current element with the start element
            swap(nums[start], nums[i]);
            // Recur for the remaining elements
            backtrack(result, nums, start + 1);
            // Backtrack by swapping the elements back
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
- Use backtracking to generate all permutations of an array.
- The time complexity is O(N!) due to the N! permutations.
- The space complexity is O(N) due to the recursion stack.