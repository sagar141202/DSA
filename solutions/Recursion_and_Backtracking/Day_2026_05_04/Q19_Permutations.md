# Permutations

## Problem Statement
Given a collection of distinct numbers, return all possible permutations. For example, if the input is [1, 2, 3], a solution set is [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]. The input array will have a length between 1 and 9.

## Approach
This problem can be solved using recursion and backtracking to generate all permutations. The basic idea is to fix one element at a time and recursively generate all permutations of the remaining elements. Backtracking is used to explore all possible permutations.

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
            // Swap elements
            swap(nums[start], nums[i]);
            // Recur for next index
            backtrack(result, nums, start + 1);
            // Backtrack and swap elements back
            swap(nums[start], nums[i]);
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result = solution.permute(nums);
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
Input: [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

## Key Takeaways
- Use recursion and backtracking to solve permutation problems.
- The time complexity of generating all permutations of n elements is O(n!), as there are n! possible permutations.
- The space complexity is O(n) for storing the recursive call stack.