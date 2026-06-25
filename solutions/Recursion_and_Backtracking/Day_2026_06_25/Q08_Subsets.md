# Subsets

## Problem Statement
Given a set of distinct integers, nums, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, given nums = [1, 2, 3], the output will be [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]. The set can contain up to 20 elements, and each element can range from -10^9 to 10^9.

## Approach
The problem can be solved using recursion and backtracking. The idea is to generate all possible subsets by either including or excluding each element from the subset. This approach ensures that all possible combinations are considered.

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
    
    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& nums, int index) {
        result.push_back(current);
        for (int i = index; i < nums.size(); i++) {
            current.push_back(nums[i]);
            backtrack(result, current, nums, i + 1);
            current.pop_back();
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result = solution.subsets(nums);
    for (auto subset : result) {
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
- Recursion and backtracking can be used to generate all possible subsets of a given set.
- The time complexity is O(2^n) because each element can either be included or excluded from the subset.
- The space complexity is also O(2^n) because in the worst case, we need to store all possible subsets.