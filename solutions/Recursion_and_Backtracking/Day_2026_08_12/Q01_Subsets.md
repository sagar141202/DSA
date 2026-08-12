# Subsets

## Problem Statement
Given a set of distinct integers, return all possible subsets. The solution should be in lexicographic order. For example, given the set [1, 2, 3], the subsets are [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]. The input set is non-empty and contains at most 100 elements.

## Approach
The problem can be solved using recursion and backtracking, where each element in the set is either included or excluded from the current subset. This approach ensures all possible subsets are generated. The recursion starts with an empty subset, and each element is added to the subset in lexicographic order.

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
        vector<int> subset;
        backtrack(result, subset, nums, 0);
        return result;
    }

    void backtrack(vector<vector<int>>& result, vector<int>& subset, vector<int>& nums, int start) {
        result.push_back(subset);
        for (int i = start; i < nums.size(); i++) {
            subset.push_back(nums[i]);
            backtrack(result, subset, nums, i + 1);
            subset.pop_back();
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> subsets = solution.subsets(nums);
    for (auto subset : subsets) {
        for (auto num : subset) {
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
Output: 
[] 
[1] 
[1, 2] 
[1, 2, 3] 
[1, 3] 
[2] 
[2, 3] 
[3]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible subsets of a given set.
- Start with an empty subset and add each element in the set to the subset in lexicographic order.
- Ensure the solution has a time complexity of O(2^n) and space complexity of O(2^n) due to the recursive nature and storage of subsets.