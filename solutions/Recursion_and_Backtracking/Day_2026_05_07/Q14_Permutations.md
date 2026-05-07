# Permutations

## Problem Statement
Given a collection of distinct numbers, return all possible permutations. The solution should use recursion and backtracking to generate all permutations. For example, given the input [1, 2, 3], the output should be [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]. The input array will have a length between 1 and 6, and the elements will be between 1 and 100.

## Approach
The algorithm will use a recursive function to generate all permutations. It will iterate over each element in the input array, remove it from the array, and recursively generate all permutations of the remaining elements. The removed element will then be added to the beginning of each permutation. This process will continue until the base case is reached, at which point the function will return the permutations.

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
                // Swap the current element with the start element
                swap(nums[start], nums[i]);
                // Recursively generate all permutations
                backtrack(result, nums, start + 1);
                // Backtrack by swapping the elements back
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
- Recursion and backtracking can be used to generate all permutations of an array.
- The base case for the recursion is when the start index equals the length of the array.
- The time complexity is O(N!) because there are N! permutations of an array of length N.