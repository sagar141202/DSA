# Subsets

## Problem Statement
Given a set of distinct integers, return all possible subsets (the power set). The solution should be implemented using recursion and backtracking. The input is a vector of integers, and the output is a vector of vectors, where each inner vector represents a subset. For example, given the input `[1, 2, 3]`, the output should be `[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]`. The input size is constrained to be at most 10 elements.

## Approach
The algorithm uses recursion to generate all subsets by considering each element in the input set and deciding whether to include it in the current subset or not. This decision is made using backtracking, where we explore both possibilities (including and excluding the current element) and combine the results.

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
        vector<int> current;
        backtrack(result, current, nums, 0);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& nums, int start) {
        result.push_back(current);
        for (int i = start; i < nums.size(); i++) {
            current.push_back(nums[i]);
            backtrack(result, current, nums, i + 1);
            current.pop_back();
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
- The use of recursion and backtracking allows for an efficient exploration of all possible subsets.
- The time complexity of O(2^n) is due to the fact that each element can be either included or excluded from a subset, resulting in 2^n possible subsets.
- The space complexity of O(2^n) is due to the storage of all subsets in the result vector.