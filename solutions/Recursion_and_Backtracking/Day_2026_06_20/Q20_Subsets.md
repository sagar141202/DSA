# Subsets

## Problem Statement
Given a set of distinct integers, return all possible subsets (the power set). The solution should be able to handle a set of size up to 20. For example, given the set [1, 2, 3], the subsets are `[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]`. The input set will not contain duplicate elements and will contain at most 20 elements.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will generate all subsets by either including or excluding each element from the subset. This ensures that we consider all possible combinations of elements.

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
        cout << "] ";
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
- Use recursion and backtracking to generate all possible subsets of a given set.
- The time complexity of this approach is O(2^n), where n is the size of the input set.
- The space complexity of this approach is also O(2^n), as we need to store all subsets in the result.