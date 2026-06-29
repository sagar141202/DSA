# Subsets

## Problem Statement
Given an integer array `nums` of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, given `nums = [1, 2, 3]`, the solution is `[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]`. The input array will have a length of at most 10, and all elements will be between 1 and 100.

## Approach
The problem can be solved using recursion and backtracking. We start with an empty subset and then for each element in the array, we have two choices: either include it in the current subset or not. This process is repeated for all elements, generating all possible subsets.

## Complexity
- Time: O(2^n)
- Space: O(2^n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> currentSubset;
        backtrack(result, currentSubset, nums, 0);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& currentSubset, vector<int>& nums, int start) {
        result.push_back(currentSubset);
        for (int i = start; i < nums.size(); i++) {
            currentSubset.push_back(nums[i]);
            backtrack(result, currentSubset, nums, i + 1);
            currentSubset.pop_back();
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> subsets = solution.subsets(nums);
    for (auto subset : subsets) {
        cout << "[";
        for (int i = 0; i < subset.size(); i++) {
            cout << subset[i];
            if (i < subset.size() - 1) {
                cout << ", ";
            }
        }
        cout << "]" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: [1, 2, 3]
Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
```

## Key Takeaways
- Recursion and backtracking can be used to generate all possible subsets of a given array.
- The time complexity of this solution is O(2^n) because we are generating all possible subsets, and there are 2^n subsets for an array of size n.
- The space complexity is also O(2^n) because we need to store all subsets in the result.