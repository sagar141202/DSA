# Subsets

## Problem Statement
Given a set of distinct integers, return all possible subsets (the power set). The solution should be able to handle sets of up to 20 integers. For example, given the set `[1, 2, 3]`, the subsets are `[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]`. The input will be a vector of integers, and the output should be a vector of vectors, where each inner vector represents a subset.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will generate all subsets by iteratively adding each element to the current subset, and then recursively generating all subsets of the remaining elements. The base case for the recursion is when the input set is empty, in which case the only subset is the empty set.

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
- The recursion and backtracking approach can be used to generate all possible subsets of a set.
- The time complexity of the solution is O(2^n) because there are 2^n possible subsets of a set with n elements.
- The space complexity of the solution is O(2^n) because we need to store all subsets in the result vector.