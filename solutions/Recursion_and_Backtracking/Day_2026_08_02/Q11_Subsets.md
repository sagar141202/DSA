# Subsets

## Problem Statement
Given a set of distinct integers, return all possible subsets (the power set). The solution should be implemented using recursion and backtracking. The input is a vector of integers, and the output should be a vector of vectors, where each inner vector represents a subset. For example, given the input [1, 2, 3], the output should be [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]. The input size is limited to 20 elements, and each element is a 32-bit integer.

## Approach
The solution uses recursion and backtracking to generate all possible subsets. It starts with an empty subset and recursively adds each element to the current subset, exploring all possible combinations. The algorithm ensures that each subset is unique and that the power set is generated efficiently.

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
    for (const auto& subset : subsets) {
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
Input: [0]
Output: [[], [0]]
```

## Key Takeaways
- Recursion and backtracking can be used to generate all possible subsets of a given set.
- The time complexity of this solution is O(2^n), where n is the size of the input set, because each element can be either included or excluded from a subset.
- The space complexity is also O(2^n) because in the worst case, the solution needs to store all possible subsets.